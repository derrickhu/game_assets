from pathlib import Path
from PIL import Image

BASE = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui')
FILES = [
    'frame_fragment_red.png',
    'frame_fragment_blue.png',
    'frame_fragment_green.png',
    'frame_fragment_yellow.png',
    'frame_fragment_brown.png',
    'frame_fragment_gray.png',
]


def make_square(path: Path) -> None:
    img = Image.open(path).convert('RGBA')
    w, h = img.size
    print(f'Before: {path.name} -> {w}x{h}')
    if w == h:
        print('  already square')
        return

    if w > h:
        # 横向更宽，左右各裁掉一点，保留中间区域
        delta = w - h
        left = delta // 2
        right = left + h
        box = (left, 0, right, h)
    else:
        # 纵向更高，上下各裁掉一点，保留中间区域
        delta = h - w
        top = delta // 2
        bottom = top + w
        box = (0, top, w, bottom)

    img = img.crop(box)
    w2, h2 = img.size
    assert w2 == h2, (w2, h2)
    img.save(path)
    print(f'After:  {path.name} -> {w2}x{h2}')


if __name__ == '__main__':
    for name in FILES:
        make_square(BASE / name)
