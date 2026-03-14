from pathlib import Path
from PIL import Image
import numpy as np

FILE = Path('/Users/huyi/rosa_games/game_assets/xiaochu/assets/images/ui/banner_reward.png')
PAD = 4
LOW, HIGH = 0.15, 0.45  # greenness thresholds


def process() -> None:
    img = Image.open(FILE).convert('RGBA')
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

    # 计算 0~1 alpha 掩码：greenness 越高越透明
    alpha_mask = np.clip((greenness - LOW) / (HIGH - LOW), 0.0, 1.0)
    new_alpha = a * (1.0 - alpha_mask)

    # 轻微去除绿溢出：把边缘区域的 g 往 max(r,b) 拉
    edge = (alpha_mask > 0) & (alpha_mask < 1.0)
    spill_replacement = max_rb
    blend = alpha_mask
    new_g = np.where(edge, g * (1.0 - blend) + spill_replacement * blend, g)

    # 完全绿的地方直接用 max_rb 替代 g
    full_green = alpha_mask >= 1.0
    new_g = np.where(full_green, spill_replacement, new_g)

    data[..., 1] = new_g
    data[..., 3] = new_alpha

    res = Image.fromarray(data.astype(np.uint8), 'RGBA')

    # 按 alpha 裁剪，四周留 PAD 像素
    alpha = res.split()[-1]
    bbox = alpha.getbbox()
    if bbox:
        x0, y0, x1, y1 = bbox
        x0 = max(0, x0 - PAD)
        y0 = max(0, y0 - PAD)
        x1 = min(res.width, x1 + PAD)
        y1 = min(res.height, y1 + PAD)
        res = res.crop((x0, y0, x1, y1))

    res.save(FILE)
    print(f'Saved {FILE} -> {res.size[0]}x{res.size[1]}')


if __name__ == '__main__':
    process()
