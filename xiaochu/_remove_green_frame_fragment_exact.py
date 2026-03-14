from pathlib import Path
from PIL import Image
import numpy as np

P = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/frame_fragment.png')

# 针对纯 #00FF00 绿底做颜色距离抠图+自动裁剪
TH_BG = 20.0   # 完全背景阈值
TH_SOFT = 40.0 # 过渡带上限
PAD = 4


def process() -> None:
    img = Image.open(P).convert('RGBA')
    arr = np.array(img, dtype=np.float32)

    r = arr[..., 0]
    g = arr[..., 1]
    b = arr[..., 2]
    a = arr[..., 3]

    # 距离纯绿色 (0,255,0) 的欧式距离
    dist = np.sqrt((r - 0.0) ** 2 + (g - 255.0) ** 2 + (b - 0.0) ** 2)

    # 完全背景：直接 alpha=0
    bg = dist <= TH_BG
    a = np.where(bg, 0.0, a)

    # 过渡区域：根据距离线性插值 alpha（越接近背景越透明）
    soft = (dist > TH_BG) & (dist < TH_SOFT)
    if np.any(soft):
        t = (dist - TH_BG) / (TH_SOFT - TH_BG)  # TH_BG->0, TH_SOFT->1
        t = np.clip(t, 0.0, 1.0)
        a = np.where(soft, a * t, a)

    arr[..., 3] = a

    out = Image.fromarray(arr.astype(np.uint8), 'RGBA')

    # 根据 alpha 自动裁剪，四周留 PAD 像素
    alpha = out.split()[-1]
    bbox = alpha.getbbox()
    if bbox:
        x0, y0, x1, y1 = bbox
        x0 = max(0, x0 - PAD)
        y0 = max(0, y0 - PAD)
        x1 = min(out.width, x1 + PAD)
        y1 = min(out.height, y1 + PAD)
        out = out.crop((x0, y0, x1, y1))

    out.save(P)
    print(f'Removed pure green background and cropped: {P} -> {out.size[0]}x{out.size[1]}')


if __name__ == '__main__':
    process()
