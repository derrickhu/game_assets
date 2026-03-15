#!/usr/bin/env python3
"""
Generate pet art using Gemini image generation, then process it.
This is a convenience wrapper that combines generation + processing.
"""
import sys
import subprocess
from pathlib import Path

GEMINI_SKILL = Path.home() / ".codebuddy/skills/gemini-image-gen/scripts/generate_images.py"


def generate_and_process(
    prompt_file: Path,
    output_dir: Path,
    pet_id: str,
    variant: str = "normal",
    aspect_ratio: str = "16:9",
    model: str = "gemini-3.1-flash-image-preview",
) -> None:
    """
    1. Generate 2:1 combined image using Gemini
    2. Process it (split, remove bg, trim, make avatar 1:1)
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Generate combined image
    combined_name = f"{pet_id}_{variant}_combined.png"
    combined_path = output_dir / combined_name

    print(f"🎨 Generating {combined_name}...")
    cmd = [
        "python3",
        str(GEMINI_SKILL),
        "--prompt-file",
        str(prompt_file),
        "--output",
        str(combined_path),
        "--model",
        model,
        "--aspect-ratio",
        aspect_ratio,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Generation failed:\n{result.stderr}", file=sys.stderr)
        raise SystemExit(1)
    print(result.stdout)

    # Step 2: Process the generated image
    avatar_name = f"{pet_id}_avatar.png" if variant == "normal" else f"{pet_id}_{variant}_avatar.png"
    full_name = f"{pet_id}.png" if variant == "normal" else f"{pet_id}_{variant}.png"

    avatar_out = output_dir / avatar_name
    full_out = output_dir / full_name

    print(f"\n🔪 Processing {combined_name}...")
    process_script = Path(__file__).parent / "process_pet_image.py"
    cmd2 = ["python3", str(process_script), str(combined_path), str(avatar_out), str(full_out)]
    result2 = subprocess.run(cmd2, capture_output=True, text=True)
    if result2.returncode != 0:
        print(f"❌ Processing failed:\n{result2.stderr}", file=sys.stderr)
        raise SystemExit(1)
    print(result2.stdout)

    print(f"\n✅ Complete! Generated:")
    print(f"   - {avatar_out}")
    print(f"   - {full_out}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: python generate_pet.py PROMPT_FILE OUTPUT_DIR PET_ID [normal|awakened]",
            file=sys.stderr,
        )
        raise SystemExit(1)

    prompt_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    pet_id = sys.argv[3]
    variant = sys.argv[4] if len(sys.argv) > 4 else "normal"

    if not prompt_file.exists():
        print(f"❌ Prompt file not found: {prompt_file}", file=sys.stderr)
        raise SystemExit(1)

    generate_and_process(prompt_file, output_dir, pet_id, variant)
