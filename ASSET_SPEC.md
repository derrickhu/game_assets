# 美术资产规范

## 命名规则

### 总体格式

```
<类型前缀>_<元素/描述>_<编号>.<格式>
```

- 全部使用 **小写英文 + 下划线**
- 禁止空格、中文、特殊字符

### 类型前缀

| 前缀 | 含义 | 所属目录 | 示例 |
|------|------|---------|------|
| `bg_` | 背景 | backgrounds/ battle/ | `bg_boss_e1.jpg` |
| `boss_` | Boss | enemies/ | `boss_f3.png` |
| `elite_` | 精英怪 | enemies/ | `elite_m2.png` |
| `mon_` | 普通怪 | enemies/ | `mon_w5.png` |
| `pet_` | 宠物 | pets/ | `pet_e12.png` |
| `fabao_` | 法宝 / 装备 | equipment/ | `fabao_w30.png` |
| `orb_` | 元素球 | orbs/ | `orb_fire.png` |
| `btn_` | 按钮 | ui/ | `btn_attack.png` |
| `icon_` | 图标 | ui/ | `icon_gold.png` |
| `panel_` | 面板 | ui/ | `panel_info.png` |
| `share_` | 分享图 | share/ | `share_cover.jpg` |
| `hero_` | 英雄 | hero/ | `hero_avatar.jpg` |

### 元素码（五行）

| 代码 | 元素 |
|------|------|
| `e` | 土 (Earth) |
| `f` | 火 (Fire) |
| `m` | 金 (Metal) |
| `s` | 水 (Water) |
| `w` | 木 (Wood) |

## 格式要求

| 用途 | 推荐格式 | 说明 |
|------|---------|------|
| 背景、场景、分享图 | `.jpg` | 不需要透明通道，文件更小 |
| 角色、UI、图标 | `.png` | 需要透明通道 |
| 设计源文件 | `.psd` | 如需存入仓库放至 `_source/` 子目录 |

## 目录规范

- 按 **功能** 划分一级子目录
- 目录名全小写，单数形式（`hero` 非 `heroes`），允许例外（`backgrounds`）
- 新增目录需在 PR 中说明用途

## 版本与标签

- 使用语义化版本标签：`v1.0.0`、`v1.1.0`
- 标签与游戏发布版本对齐
- 里程碑变更在标签描述中记录
