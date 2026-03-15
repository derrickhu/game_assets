from pathlib import Path
import re

DOC_PATH = Path('/Users/huyi/rosa_games/xiaochu/docs/灵兽秘境敌人美术提示词.md')
OUT_DIR = Path('/Users/huyi/rosa_games/game_assets/xiaochu')

text = DOC_PATH.read_text(encoding='utf-8')
lines = text.splitlines()

# 1) 找到普通形态通用模板的 code block
start_idx = None
for i, line in enumerate(lines):
    if line.strip() == '### 普通形态模板':
        start_idx = i
        break

if start_idx is None:
    raise SystemExit('UNIVERSAL_TEMPLATE_HEADING_NOT_FOUND')

code_start = None
for i in range(start_idx + 1, len(lines)):
    if lines[i].strip() == '```':
        code_start = i + 1
        break

if code_start is None:
    raise SystemExit('UNIVERSAL_TEMPLATE_CODE_START_NOT_FOUND')

code_end = None
for i in range(code_start, len(lines)):
    if lines[i].strip() == '```':
        code_end = i
        break

if code_end is None:
    raise SystemExit('UNIVERSAL_TEMPLATE_CODE_END_NOT_FOUND')

base_tpl = '\n'.join(lines[code_start:code_end]).strip()

# 2) 提取 2-5 号宠物的普通形态描述
pets: dict[str, dict] = {}
for i, line in enumerate(lines):
    m2 = re.match(r"^###\s+#(\d+)\s+(.+?)\s+\(([^)]+)\)", line.strip())
    if not m2:
        continue
    no, cn, pid = m2.groups()
    if no not in {"2", "3", "4", "5"}:
        continue
    normal_desc = None
    j = i + 1
    while j < len(lines):
        if lines[j].startswith('### #') and j != i:
            break
        if lines[j].strip().startswith('**普通形态**'):
            k = j + 1
            while k < len(lines) and lines[k].strip() != '```':
                k += 1
            if k >= len(lines):
                break
            k += 1
            desc_lines: list[str] = []
            while k < len(lines) and lines[k].strip() != '```':
                desc_lines.append(lines[k])
                k += 1
            normal_desc = '\n'.join(desc_lines).strip()
            break
        j += 1
    if not normal_desc:
        raise SystemExit(f'NORMAL_DESC_NOT_FOUND for #{no}')
    pets[no] = {"no": no, "name_cn": cn, "pet_id": pid, "normal": normal_desc}

for no in sorted(pets.keys(), key=int):
    pet = pets[no]
    pid = pet['pet_id']
    normal = pet['normal']
    prompt = base_tpl + f"\n\nSUBJECT — {pid} (normal form): {normal}\n"
    out_path = OUT_DIR / f'_prompt_{pid}_normal.txt'
    out_path.write_text(prompt, encoding='utf-8')
    print(f"WROTE {out_path} for #{no} {pid}")
