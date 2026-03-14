from pathlib import Path
from PIL import Image, ImageFile
import numpy as np

ImageFile.LOAD_TRUNCATED_IMAGES = True

BASE = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/hero')
FILES = [
    'char_boy2_nobg.png',
    'char_girl2_nobg.png',
    'char_girl3_nobg.png',
]

LOW, HIGH = 0.10, 0.40


def process_one(path: Path) -> None:
    img = Image.open(path).convert('RGBA')
    data = np.array(img, dtype=np.float32)

    r = data[..., 0]
    g = data[..., 1]
    b = data[..., 2]
    a = data[..., 3]

    max_rb = np.maximum(r, b)
    g_safe = np.where(g > 0, g, 1.0)
    dominance = np.clip((g - max_rb) / g_safe, 0.0, 1.0)
    brightness = g / 255.0
    is_green_max = (g > r) & (g > b)
    greenness = dominance * brightness * is_green_max.astype(np.float32)

    edge_like = (a > 0) & (a < 255)
    mask = (greenness > LOW) & edge_like
    if not np.any(mask):
        print(f'No green spill to black: {path.name}')
        return

    t = np.clip((greenness - LOW) / (HIGH - LOW), 0.0, 1.0)

    for ch in range(3):
        c = data[..., ch]
        c_new = c * (1.0 - t)
        data[..., ch] = np.where(mask, c_new, c)

    strong = (greenness >= HIGH) & edge_like
    data[..., 3] = np.where(strong, a * 0.6, a)

    out = Image.fromarray(data.astype(np.uint8), 'RGBA')
    out.save(path)
    print(f'Despilled-to-black {path.name}')


def main() -> None:
    for name in FILES:
        p = BASE / name
        if not p.exists():
            print(f'Skip missing: {p}')
            continue
        process_one(p)


if __name__ == '__main__':
    main()
