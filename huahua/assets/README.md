# 花花草草 · 美术资源（仓库外）

本目录存放 **AI 原始出图、抠图中间件、待确认版本**，不进入 `huahua` 游戏仓库。  
**只有定稿** 再拷贝到：`huahua/minigame/images/flowers/green/flower_green_*.png`。

## 绿植线 BN2 1:1（`green_plant_nb2/`）

| 子目录 | 内容 |
|--------|------|
| `raw/` | Gemini NB2 直出，品红底 `#FF00FF` |
| `nobg/` | `rembg`（默认 `birefnet-general-lite`） |
| `final/` | `crop_trim` + 品红键清理；另有 `flower_green_N.png` 与 `flower_green_N_nb2_1x1.png` 同内容 |

提示词：

- Lv1/2/4/6/9/10：`huahua/docs/prompt/green_1_2_4_6_9_10_nb2_square_prompt.txt`
- Lv3/5/7/8：`huahua/docs/prompt/green_3_5_7_8_nb2_square_prompt.txt`

## 冷饮线 BN2 网格（待确认）

**当前推荐：**

- `drink_cold_nb2/for_review/drink_cold_1to4_nb2_sheet_v2.png` — Lv1–4（无文字；第 4 杯玫瑰冰沙改为光滑杯口、无颗粒糖霜边，便于抠图）
- `drink_cold_nb2/for_review/drink_cold_5to8_nb2_sheet_v3.png` — Lv5–8（强调无文字；装饰更紧凑，避免细条柠檬皮伸太长）

旧版 `drink_cold_1to4_nb2_sheet.png`、`drink_cold_5to8_nb2_sheet*.png`（非 v2/v3）可作归档或删除。

**切图若仍带上下文字条：** 先用工具裁掉整图顶/底标题区，再 `split_grid 4 1`；或加大 `--margin` 只保留饮品主体区。

提示词：`huahua/docs/prompt/drink_cold_1to4_nb2_sheet_prompt.txt`、`drink_cold_5to8_nb2_sheet_prompt.txt`  
**确认后再** `split_grid` → rembg → 拷贝到 `huahua/minigame/images/drinks/cold/drink_cold_*.png`。

### 冷饮线 · 带等级递进（推荐先看）

- `drink_cold_nb2/for_review/progression_1x1/drink_cold_{1..8}_nb2_progression_1x1.png` — 8 张独立 **1:1** 原图（品红底）。
- `drink_cold_nb2/processed/nobg/`、`drink_cold_nb2/processed/final/` — 抠图 / 裁切后中间件。
- **已部署到游戏：** `huahua/minigame/images/drinks/cold/drink_cold_1.png` … `drink_cold_8.png`（`birefnet-general-lite` + trim + 品红键清理）。
- 说明与进阶表：`huahua/docs/prompt/drink_cold_1to8_progression_nb2.md`
- 重新生成脚本：`huahua/scripts/gen_drink_cold_progression_nb2.py`

### 茶饮 / 甜品线 NB2（1:1 ×8）

- 原图：`drink_tea_nb2/for_review/1x1/`、`drink_dessert_nb2/for_review/1x1/`
- 生成：`python3 huahua/scripts/gen_drink_tea_dessert_nb2.py`（可加 `--line tea` / `dessert`）
- 抠图进包：`python3 huahua/scripts/process_drink_tea_dessert_nb2.py`
- 说明：`huahua/docs/prompt/drink_tea_dessert_nb2_progression.md`
