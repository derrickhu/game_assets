from pathlib import Path
from PIL import Image
import numpy as np

SRC = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/btn_stage_select.png')
OUT = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/btn_stage_select_nobg.png')

PAD = 4
LOW, HIGH = 0.03, 0.12  # brightness thresholds for black background keying


def process():
    img = Image.open(SRC).convert('RGBA')
    arr = np.array(img, dtype=np.float32)

    rgb = arr[..., :3]
    a = arr[..., 3]

    max_rgb = rgb.max(axis=2)
    brightness = max_rgb / 255.0

    # brightness < LOW -> alpha 0, > HIGH -> alpha 原值，中间平滑过渡
    factor = np.clip((brightness - LOW) / (HIGH - LOW), 0.0, 1.0)
    arr[..., 3] = a * factor

    res = Image.fromarray(arr.astype('uint8'), 'RGBA')

    # 根据 alpha 自动裁剪，四周留 PAD 像素
    alpha = res.split()[-1]
    bbox = alpha.getbbox()
    if bbox:
        x0, y0, x1, y1 = bbox
        x0 = max(0, x0 - PAD)
        y0 = max(0, y0 - PAD)
        x1 = min(res.width, x1 + PAD)
        y1 = min(res.height, y1 + PAD)
        res = res.crop((x0, y0, x1, y1))

    res.save(OUT)
    print(f'Saved {OUT} -> {res.size[0]}x{res.size[1]}')


if __name__ == '__main__':
    process()
