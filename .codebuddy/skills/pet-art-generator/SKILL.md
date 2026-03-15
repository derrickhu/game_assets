---
name: pet-art-generator
description: This skill should be used when generating game pet/character art assets that require a specific workflow - AI image generation (via Gemini), automatic splitting of combined avatar+full-body images, background removal (rembg), and ensuring avatars are 1:1 square format. Triggers on requests to generate game pet art, character sprites with avatar/full-body variants, or when working with Chinese ink-wash style game assets that need processing.
---

# Pet Art Generator

## Overview

Generate and process game pet/character art assets using an automated pipeline: AI image generation → split combined images → background removal → auto-crop → ensure avatar 1:1 ratio.

This skill is designed for game art workflows where a single 2:1 landscape image contains both an avatar (left half) and full-body sprite (right half), requiring automatic processing into separate assets.

## When to Use This Skill

Use this skill when:
- Generating game pet/character art with both avatar and full-body variants
- Working with 2:1 combined images that need splitting and processing
- Requiring background removal (matting) for game sprites
- Ensuring avatars are strictly 1:1 square format after processing
- Processing Chinese ink-wash style game assets (as per the included prompt templates)

## Workflow

### 1. Quick Start - Full Pipeline

For a complete generation + processing pipeline:

```bash
python3 {SKILL_DIR}/scripts/generate_pet.py \
    PROMPT_FILE \
    OUTPUT_DIR \
    PET_ID \
    [normal|awakened]
```

**Parameters:**
- `PROMPT_FILE`: Path to text file containing the full AI generation prompt
- `OUTPUT_DIR`: Directory where processed assets will be saved
- `PET_ID`: Identifier for the pet (e.g., `rock_badger`)
- `normal|awakened`: Variant type (optional, defaults to `normal`)

**Output files:**
- `{OUTPUT_DIR}/{PET_ID}_avatar.png` - 1:1 square avatar, background removed
- `{OUTPUT_DIR}/{PET_ID}.png` - Full-body sprite, background removed
- `{OUTPUT_DIR}/{PET_ID}_normal_combined.png` - Original generated 2:1 image (preserved)

For awakened variant, files are named `{PET_ID}_awakened_avatar.png` and `{PET_ID}_awakened.png`.

**Example:**

```bash
# Generate rock badger normal form
python3 ~/.codebuddy/skills/pet-art-generator/scripts/generate_pet.py \
    /path/to/rock_badger_normal_prompt.txt \
    ./assets/images \
    rock_badger \
    normal
```

### 2. Processing Only (Skip Generation)

To process an existing 2:1 combined image:

```bash
python3 {SKILL_DIR}/scripts/process_pet_image.py \
    COMBINED_IMAGE \
    AVATAR_OUTPUT \
    FULL_OUTPUT
```

**Parameters:**
- `COMBINED_IMAGE`: Path to 2:1 landscape source image
- `AVATAR_OUTPUT`: Where to save the processed avatar (will be 1:1)
- `FULL_OUTPUT`: Where to save the processed full-body sprite

**Processing steps:**
1. Split 2:1 image into left (avatar) and right (full-body)
2. Remove background using `rembg` with `birefnet-general` model
3. Trim transparent edges (auto-crop to content bounding box)
4. Make avatar 1:1 square (top-aligned crop to preserve head/upper body)
5. Save both outputs as PNG with transparency

**Example:**

```bash
python3 ~/.codebuddy/skills/pet-art-generator/scripts/process_pet_image.py \
    ./assets/images/rock_badger_normal_combined.png \
    ./assets/images/rock_badger_avatar.png \
    ./assets/images/rock_badger.png
```

## Technical Details

### Background Removal

- **Model**: `birefnet-general` via `rembg` (928MB, ~9.5s on Apple Silicon)
- **Execution**: CPU-only (`CPUExecutionProvider`), optimized with `OMP_NUM_THREADS=8`
- **Quality**: High-quality edge detection suitable for game sprites

Alternative models can be used by modifying `MODEL` in the scripts:
- `birefnet-general-lite` - Faster (214MB, ~4.6s) but lower quality
- `u2net` - Basic quality (176MB, ~3s)
- `isnet-anime` - Optimized for anime/illustration style (168MB, ~3s)

### Avatar 1:1 Cropping

The avatar processing uses **top-aligned square crop**:
- After background removal and alpha trimming, if the avatar is taller than wide, it crops from the top
- This preserves the head and upper body while removing excess lower body or residual background
- Ensures the final avatar is always a perfect square (N×N pixels)

### Image Generation

Uses Gemini AI image generation via the `gemini-image-gen` skill:
- **Default model**: `gemini-3.1-flash-image-preview` (Nano Banana 2)
- **Aspect ratio**: 16:9 (approximates 2:1 for the combined layout)
- **Output**: PNG with consistent quality for game assets

## Prompt Templates

The `references/prompt_templates.md` file contains comprehensive Chinese ink-wash style prompt templates for game pets, including:
- Universal style definitions (calligraphy brush outlines, ink wash coloring)
- 2:1 layout specifications (left half = avatar close-up, right half = full-body battle pose)
- 33 pet character descriptions with normal + awakened variants
- Strict formatting requirements for clean background removal

**To use the templates:**
1. Read `references/prompt_templates.md` to find the desired pet
2. Combine the universal template + specific pet description into a prompt file
3. Run `generate_pet.py` with that prompt file

**Example workflow:**

```bash
# 1. Extract prompt for rock_badger normal form
cat > /tmp/rock_badger_prompt.txt << 'EOF'
A single 2:1 landscape image split into two equal halves on one canvas...
[universal template]
...
SUBJECT — rock_badger (normal form): A young badger spirit with...
EOF

# 2. Generate and process
python3 ~/.codebuddy/skills/pet-art-generator/scripts/generate_pet.py \
    /tmp/rock_badger_prompt.txt \
    ./assets/images \
    rock_badger \
    normal
```

## Dependencies

**Python packages required:**
- `rembg` >= 2.0
- `onnxruntime` >= 1.19
- `Pillow` (PIL)

**External skills:**
- `gemini-image-gen` skill must be available at `~/.codebuddy/skills/gemini-image-gen`

**Environment:**
- Python 3.7+
- Tested on macOS (Apple Silicon optimized)
- Model cache: `~/.u2net/` (created automatically on first run)

## File Organization

This skill includes:

### scripts/
- `generate_pet.py` - Full pipeline wrapper (generation + processing)
- `process_pet_image.py` - Standalone processing script (split, remove bg, crop)

### references/
- `prompt_templates.md` - Complete prompt templates for 33 game pets (normal + awakened variants)

### assets/
- (None) - This skill does not bundle asset files
