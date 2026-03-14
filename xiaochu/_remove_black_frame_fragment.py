from pathlib import Path
from PIL import Image
import numpy as np

P = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/frame_fragment.png')

# 基于亮度抠掉纯黑背景
LOW, HIGH = 0.03, 0.12  # brightness thresholds
PAD = 0


def process() -> None:
    img = Image.open(P).convert('RGBA')
    arr = np.array(img, dtype=np.float32)

    rgb = arr[..., :3]
    # 初始 alpha 全部设为不透明
    a = np.full(arr.shape[:2], 255.0, dtype=np.float32)

    max_rgb = rgb.max(axis=2)
    brightness = max_rgb / 255.0

    # brightness < LOW -> 完全透明; > HIGH -> 完全不透明; 中间线性过渡
    factor = np.clip((brightness - LOW) / (HIGH - LOW), 0.0, 1.0)
    a = a * factor

    arr[..., 3] = a

    out = Image.fromarray(arr.astype(np.uint8), 'RGBA')

    # 根据 alpha 自动裁剪，四周留 PAD 像素
    alpha = out.split()[-1]
    bbox = alpha.getbbox()
    if bbox:
        x0, y0, x1, y1 = bbox
        # 先按 PAD 处理，然后额外从左和上各再收 4 像素
        x0 = max(0, x0 - PAD + 4)
        y0 = max(0, y0 - PAD + 4)
        x1 = min(out.width, x1 + PAD)
        y1 = min(out.height, y1 + PAD)
        out = out.crop((x0, y0, x1, y1))

    out.save(P)
    print(f'Removed black background and cropped: {P} -> {out.size[0]}x{out.size[1]}')


if __name__ == '__main__':
    process()
