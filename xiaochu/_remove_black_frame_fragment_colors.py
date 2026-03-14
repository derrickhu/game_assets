from pathlib import Path
from PIL import Image
import numpy as np

FILES = [
    Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/frame_fragment_red.png'),
    Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/frame_fragment_blue.png'),
    Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/frame_fragment_green.png'),
    Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/frame_fragment_yellow.png'),
    Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/frame_fragment_brown.png'),
    Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/frame_fragment_gray.png'),
]

LOW, HIGH = 0.03, 0.12  # brightness thresholds
PAD = 0


def process(p: Path) -> None:
    img = Image.open(p).convert('RGBA')
    arr = np.array(img, dtype=np.float32)

    rgb = arr[..., :3]
    a = np.full(arr.shape[:2], 255.0, dtype=np.float32)

    max_rgb = rgb.max(axis=2)
    brightness = max_rgb / 255.0

    factor = np.clip((brightness - LOW) / (HIGH - LOW), 0.0, 1.0)
    a = a * factor

    arr[..., 3] = a

    out = Image.fromarray(arr.astype(np.uint8), 'RGBA')

    alpha = out.split()[-1]
    bbox = alpha.getbbox()
    if bbox:
        x0, y0, x1, y1 = bbox
        x0 = max(0, x0 - PAD)
        y0 = max(0, y0 - PAD)
        x1 = min(out.width, x1 + PAD)
        y1 = min(out.height, y1 + PAD)
        out = out.crop((x0, y0, x1, y1))

    out.save(p)
    print(f'Removed black background and cropped: {p} -> {out.size[0]}x{out.size[1]}')


if __name__ == '__main__':
    for p in FILES:
        process(p)
