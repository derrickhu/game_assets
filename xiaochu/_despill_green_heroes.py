from pathlib import Path
from PIL import Image
import numpy as np

BASE = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/hero')
FILES = [
    'char_boy1_nobg.png',
    'char_boy2_nobg.png',
    'char_boy3_nobg.png',
    'char_girl1_nobg.png',
    'char_girl2_nobg.png',
    'char_girl3_nobg.png',
]

# 绿溢出强度阈值
LOW, HIGH = 0.20, 0.60  # >LOW 开始去绿, >HIGH 视为纯绿背景


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

    # 只在已有一点透明度的区域做处理，避免破坏完全实心的内部绿色细节
    edge_like = (a > 0) & (a < 255)
    mask = (greenness > LOW) & edge_like
    if not np.any(mask):
        print(f'No green spill: {path.name}')
        return

    # 计算 0~1 的去绿强度
    t = np.clip((greenness - LOW) / (HIGH - LOW), 0.0, 1.0)

    # 绿色通道往 max(r,b) 方向拉，削弱鲜绿色
    new_g = g * (1.0 - t) + max_rb * t
    g = np.where(mask, new_g, g)

    # 对非常绿的像素顺带再降一点 alpha，减轻边缘光晕
    strong = (greenness >= HIGH) & edge_like
    new_a = np.where(strong, a * 0.3, a)

    data[..., 1] = g
    data[..., 3] = new_a

    out = Image.fromarray(data.astype(np.uint8), 'RGBA')
    out.save(path)
    print(f'Despilled {path.name}')


def main() -> None:
    for name in FILES:
        p = BASE / name
        if not p.exists():
            print(f'Skip missing: {p}')
            continue
        process_one(p)


if __name__ == '__main__':
    main()
