from pathlib import Path
from PIL import Image
import numpy as np

SRC = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/nav_battle.png')
OUT = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/nav_battle_nobg.png')

PAD = 4
LOW, HIGH = 0.03, 0.12  # brightness thresholds for black background keying


def process():
    img = Image.open(SRC).convert('RGBA')
    arr = np.array(img, dtype=np.float32)

    r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
    max_rgb = np.maximum(np.maximum(r, g), b)
    brightness = max_rgb / 255.0

    factor = np.clip((brightness - LOW) / (HIGH - LOW), 0.0, 1.0)
    new_a = a * factor
    arr[..., 3] = new_a

    res = Image.fromarray(arr.astype('uint8'), 'RGBA')

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
