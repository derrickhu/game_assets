# Game Assets

游戏美术资源管理仓库，使用 Git LFS 管理二进制资产。

## 项目

| 项目 | 目录 | 说明 |
|------|------|------|
| 消除 (xiaochu) | `xiaochu/` | 消除类游戏美术资源 |

## 快速开始

### 克隆仓库

```bash
# 确保已安装 Git LFS
git lfs install

# 克隆（会自动拉取 LFS 文件）
git clone git@github.com:derrickhu/game_assets.git
```

### 分支规范

| 分支 | 用途 |
|------|------|
| `main` | 正式发布的资源，与游戏版本对齐 |
| `dev` | 日常开发整合 |
| `feat/<项目>-<描述>` | 新增资源，如 `feat/xiaochu-new-pets` |
| `fix/<项目>-<描述>` | 修正资源，如 `fix/xiaochu-hero-avatar` |

### 提交流程

1. 从 `dev` 创建功能分支
2. 添加 / 修改资源
3. 提交并推送（提交信息遵循[约定式提交](https://www.conventionalcommits.org/)）
4. 创建 Pull Request，附预览截图
5. Review 通过后合入 `dev`

## 目录结构

```
game_assets/
├── xiaochu/
│   └── assets/
│       ├── backgrounds/    # 背景图
│       ├── battle/         # 战斗场景
│       ├── enemies/        # 敌人 / 怪物
│       ├── equipment/      # 装备（法宝）
│       ├── hero/           # 英雄 / 主角
│       ├── orbs/           # 元素球
│       ├── pets/           # 宠物
│       ├── share/          # 分享相关
│       └── ui/             # 界面元素
└── ...
```

## 相关文档

- [美术资产规范](ASSET_SPEC.md)
