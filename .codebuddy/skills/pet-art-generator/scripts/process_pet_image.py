#!/usr/bin/env python3
"""
Process combined pet image: split → remove background → trim → make avatar 1:1 with safe margin
"""
import os, sys
from pathlib import Path
from typing import Tuple

os.environ["OMP_NUM_THREADS"] = "8"

from rembg import remove, new_session  # type: ignore
from PIL import Image  # type: ignore

MODEL = "birefnet-general"
PROVIDERS = ["CPUExecutionProvider"]


def split_avatar_full(src: Path) -> Tuple[Image.Image, Image.Image]:
    """Split 2:1 landscape image into left (avatar) and right (full body)."""
    img = Image.open(src).convert("RGBA")
    w, h = img.size
    mid = w // 2
    left = img.crop((0, 0, mid, h))
    right = img.crop((mid, 0, w, h))
    return left, right


def trim_alpha(im: Image.Image) -> Image.Image:
    """Crop image to the bounding box of non-transparent pixels."""
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
        # keep top part, crop bottom
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


def process_pet(
    combined_path: Path,
    avatar_out: Path,
    full_out: Path,
    model: str = MODEL,
) -> None:
    """
    Process a 2:1 combined pet image:
    1. Split into left (avatar) and right (full body)
    2. Remove background using rembg
    3. Trim transparent edges
    4. Make avatar 1:1 (centered) and add safe margin
    5. Save both outputs
    """
    if not combined_path.exists():
        raise FileNotFoundError(f"Source image not found: {combined_path}")

    print(f"Processing: {combined_path}")
    print(f"  Loading model: {model}...")
    session = new_session(model, providers=PROVIDERS)

    avatar_img, full_img = split_avatar_full(combined_path)
    print(f"  Split into avatar ({avatar_img.size}) and full ({full_img.size})")

    print(f"  Removing backgrounds...")
    avatar_rgba = remove(avatar_img, session=session)
    full_rgba = remove(full_img, session=session)

    print(f"  Trimming alpha edges...")
    avatar_rgba = trim_alpha(avatar_rgba)
    full_rgba = trim_alpha(full_rgba)

    print(f"  Making avatar 1:1 (centered)...")
    # 对头像使用居中裁剪，避免切掉下巴或耳朵
    avatar_rgba = make_square(avatar_rgba, align_top=False)

    print(f"  Adding avatar safe margin (scale=0.8)...")
    avatar_rgba = add_avatar_margin(avatar_rgba, scale=0.8)

    avatar_out.parent.mkdir(parents=True, exist_ok=True)
    full_out.parent.mkdir(parents=True, exist_ok=True)

    avatar_rgba.save(avatar_out)
    full_rgba.save(full_out)
    print(f"✅ Saved avatar: {avatar_out} ({avatar_rgba.size})")
    print(f"✅ Saved full:   {full_out} ({full_rgba.size})")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: python process_pet_image.py COMBINED_IMAGE AVATAR_OUT FULL_OUT",
            file=sys.stderr,
        )
        raise SystemExit(1)

    combined = Path(sys.argv[1])
    avatar = Path(sys.argv[2])
    full = Path(sys.argv[3])

    process_pet(combined, avatar, full)
