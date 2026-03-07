# 《花语小筑》美术资产清单

## 目录结构

```
huahua/
├── assets/
│   ├── items/          # 游戏物品（花束、花饮、建筑等）
│   ├── ui/             # 界面元素
│   ├── backgrounds/    # 背景图
│   ├── share/          # 分享相关
│   ├── hero/           # 英雄/店主形象
│   └── equipment/      # 装备/道具
└── ASSET_LIST.md       # 本文件
```

## 命名规范

遵循 [ASSET_SPEC.md](../ASSET_SPEC.md) 规范：

### 物品资源 (items/)
- `item_flower_<花系>_<等级>.png` - 花束物品
- `item_drink_<饮品线>_<等级>.png` - 花饮物品
- `item_building_<类型>_<编号>.png` - 建筑物品
- `item_chest_<等级>.png` - 宝箱

### 花系代码
- `daily` - 日常花系（暖黄绿色调）
- `romantic` - 浪漫花系（粉紫红色调）
- `luxury` - 奢华花系（金蓝银色调）

### 饮品线代码
- `tea` - 茶饮线（暖茶棕色调）
- `cold` - 冷饮线（冰蓝清爽色调）
- `dessert` - 甜品线（粉橙甜蜜色调）

## 当前资产

### 已导入资源
### 花束资源（日常花系）

- `item_flower_daily_1.png` (976KB)
- `item_flower_daily_1_nobg.png` (419KB)
- `item_flower_daily_2.png` (1044KB)
- `item_flower_daily_2_nobg.png` (486KB)
- `item_flower_daily_3.png` (1093KB)
- `item_flower_daily_4.png` (1173KB)
- `item_flower_daily_5.png` (1196KB)
- `item_flower_daily_6.png` (1272KB)

## 待补充资源

根据美术资源清单，需要补充以下资源：

### 花束系（18种）
- 日常花系：6级（已部分完成）
- 浪漫花系：6级
- 奢华花系：6级

### 花饮系（9种）
- 茶饮线：3级
- 冷饮线：3级
- 甜品线：3级

### 建筑与功能物品（23种）
- 永久建筑：7种
- 消耗型建筑：6种
- 建筑材料：7种
- 宝箱：3种

### UI资源
- 按钮、图标、面板等
- 背景图
- 分享图

## 使用说明

1. 游戏开发时引用路径：`huahua/assets/items/item_flower_daily_1.png`
2. 新增资源请遵循命名规范
3. 提交前请更新本清单
