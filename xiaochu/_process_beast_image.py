import os, sys
from pathlib import Path
from typing import Tuple

os.environ["OMP_NUM_THREADS"] = "8"

from rembg import remove, new_session  # type: ignore
from PIL import Image  # type: ignore

MODEL = "birefnet-general"
PROVIDERS = ["CPUExecutionProvider"]


def split_avatar_full(src: Path) -> Tuple[Image.Image, Image.Image]:
    img = Image.open(src).convert("RGBA")
    w, h = img.size
    mid = w // 2
    left = img.crop((0, 0, mid, h))
    right = img.crop((mid, 0, w, h))
    return left, right


def trim_alpha(im: Image.Image) -> Image.Image:
    if im.mode != "RGBA":
        im = im.convert("RGBA")
    alpha = im.split()[3]
    bbox = alpha.getbbox()
    if not bbox:
        return im
    return im.crop(bbox)


def make_square(im: Image.Image, align_top: bool = True) -> Image.Image:
    """Crop image to 1:1. If taller than wide, prefer keeping the top (for avatars)."""
    w, h = im.size
    if w == h:
        return im
    if w > h:
        # wider than tall: center crop horizontally
        left = (w - h) // 2
        right = left + h
        return im.crop((left, 0, right, h))
    # taller than wide
    if align_top:
        # keep top part, crop bottom (更适合头像，避免露出多余身体/白边)
        return im.crop((0, 0, w, w))
    else:
        # center crop vertically
        top = (h - w) // 2
        bottom = top + w
        return im.crop((0, top, w, bottom))


def add_avatar_margin(im: Image.Image, scale: float = 0.8) -> Image.Image:
    """Shrink avatar slightly and center it on the same-size square canvas to add safe margins."""
    w, h = im.size
    if w != h:
        return im
    new_size = int(w * scale)
    if new_size >= w:
        return im
    resized = im.resize((new_size, new_size), Image.LANCZOS)
    canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    offset = ((w - new_size) // 2, (h - new_size) // 2)
    canvas.paste(resized, offset, resized)
    return canvas


def process_pet(pet_id: str, variant: str = "normal") -> None:
    base_dir = Path(__file__).resolve().parent
    assets_dir = base_dir / "assets" / "images"
    assets_dir.mkdir(parents=True, exist_ok=True)

    combined_name = f"{pet_id}_{variant}_combined.png"
    src = assets_dir / combined_name
    if not src.exists():
        raise SystemExit(f"Source image not found: {src}")

    session = new_session(MODEL, providers=PROVIDERS)

    avatar_img, full_img = split_avatar_full(src)

    avatar_rgba = remove(avatar_img, session=session)
    full_rgba = remove(full_img, session=session)

    avatar_rgba = trim_alpha(avatar_rgba)
    full_rgba = trim_alpha(full_rgba)

    # 头像保证 1:1，这里使用居中裁剪，避免切掉下巴或耳朵
    avatar_rgba = make_square(avatar_rgba, align_top=False)
    # 再缩小一点并居中，给耳朵和头顶留出安全边距
    avatar_rgba = add_avatar_margin(avatar_rgba, scale=0.8)

    if variant == "normal":
        avatar_out = assets_dir / f"{pet_id}_avatar.png"
        full_out = assets_dir / f"{pet_id}.png"
    else:
        avatar_out = assets_dir / f"{pet_id}_{variant}_avatar.png"
        full_out = assets_dir / f"{pet_id}_{variant}.png"

    avatar_rgba.save(avatar_out)
    full_rgba.save(full_out)
    print(f"Saved avatar: {avatar_out}")
    print(f"Saved full:   {full_out}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python _process_beast_image.py PET_ID [normal|awakened]", file=sys.stderr)
        raise SystemExit(1)
    pet_id = sys.argv[1]
    variant = sys.argv[2] if len(sys.argv) > 2 else "normal"
    process_pet(pet_id, variant)
