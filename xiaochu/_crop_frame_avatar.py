from pathlib import Path
from PIL import Image

P = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/frame_avatar_nobg.png')
PAD = 4


def process() -> None:
    img = Image.open(P).convert('RGBA')
    alpha = img.split()[-1]
    bbox = alpha.getbbox()
    if not bbox:
        print('No non-transparent pixels found')
        return
    x0, y0, x1, y1 = bbox
    x0 = max(0, x0 - PAD)
    y0 = max(0, y0 - PAD)
    x1 = min(img.width, x1 + PAD)
    y1 = min(img.height, y1 + PAD)
    img = img.crop((x0, y0, x1, y1))
    img.save(P)
    print(f'Cropped {P} -> {img.size[0]}x{img.size[1]}')


if __name__ == '__main__':
    process()
