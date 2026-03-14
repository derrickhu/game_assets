from pathlib import Path
from PIL import Image
import numpy as np

P = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/btn_stage_select_nobg.png')

# 亮度阈值：低于 LOW 认为太黑，逐渐透明；HIGH 以上不动
LOW, HIGH = 0.05, 0.18


def process() -> None:
    img = Image.open(P).convert('RGBA')
    arr = np.array(img, dtype=np.float32)

    rgb = arr[..., :3]
    a = arr[..., 3]

    max_rgb = rgb.max(axis=2)
    brightness = max_rgb / 255.0

    # 只处理已经有一定透明度的区域，避免改到内部正常阴影
    edge_like = (a > 0) & (a < 255)
    dark = (brightness < HIGH) & edge_like
    if not np.any(dark):
        print('No dark edge pixels to soften')
        img.save(P)
        return

    # 亮度越低，alpha 越接近 0：factor 从 0->1
    factor = np.clip((brightness - LOW) / (HIGH - LOW), 0.0, 1.0)
    new_a = a * factor

    # 只在 dark 区域应用新的 alpha
    a = np.where(dark, new_a, a)
    arr[..., 3] = a

    out = Image.fromarray(arr.astype(np.uint8), 'RGBA')
    out.save(P)
    print(f'Softened black edges -> {P}')


if __name__ == '__main__':
    process()
