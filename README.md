# Coding Skills — Cursor 开发技能工具箱

汇集 8 个上游技能，用于 UI 设计、React/Next.js、测试、调试、验收和分支交付。保留上游完整目录与原文，不把八份指令合并进一个大提示词；Agent 按任务加载需要的技能。

## 技能导航

| 场景 | 技能 | 来源 |
| --- | --- | --- |
| UI 设计 | [frontend-design](skills/frontend-design/SKILL.md) | Anthropic |
| UI 质量与可访问性审查 | [web-design-guidelines](skills/web-design-guidelines/SKILL.md) | Vercel |
| React / Next.js 性能 | [react-best-practices](skills/react-best-practices/SKILL.md) | Vercel |
| 单元测试、回归测试 | [test-driven-development](skills/test-driven-development/SKILL.md) | Superpowers |
| 浏览器功能测试 | [webapp-testing](skills/webapp-testing/SKILL.md) | Anthropic |
| 问题定位 | [systematic-debugging](skills/systematic-debugging/SKILL.md) | Superpowers |
| 最终验收 | [verification-before-completion](skills/verification-before-completion/SKILL.md) | Superpowers |
| 分支交付 | [finishing-a-development-branch](skills/finishing-a-development-branch/SKILL.md) | Superpowers |

## Mac 上安装到 Cursor

需要 Git 和 Python 3。clone 本仓库后，再进入该目录。

```bash
git clone https://github.com/Moana-ocean/Cursor_Skill_Set.git
cd Cursor_Skill_Set
# 全局安装：让不同项目都能使用
python3 scripts/install.py --global
# 或只安装到一个项目（二选一）
python3 scripts/install.py --project /Users/ocean/你的项目目录
```

全局位置是 `~/.cursor/skills/`；项目位置是 `<项目>/.cursor/skills/`。安装会复制每个技能的完整目录。遇到同名目录会停止，不覆盖你的内容；先把旧目录移到备份位置，再重新安装。可以加 `--dry-run` 预览安装位置。安装后打开新的 Cursor Agent 对话，并检查技能是否被发现。官方说明：<https://cursor.com/docs/skills>。

若使用本次提供的 Git bundle，可以直接把 bundle 当作 Git 仓库 clone：

```bash
git clone /下载路径/coding-skills.bundle coding-skills
cd coding-skills
python3 scripts/install.py --global
```

## 如何统筹使用

- 新 UI：先用 frontend-design 确定视觉方向，React 项目再结合 react-best-practices；实现后执行 UI 审查和浏览器测试。
- 修 Bug：先用 systematic-debugging 定位原因，再用 test-driven-development 添加失败回归测试并修复。
- 宣布完成前：用 verification-before-completion 执行项目实际需要的检查，提供命令输出与未解决问题。
- 需要 PR、合并或清理分支时：使用 finishing-a-development-branch，并先确认交付目标。

可直接给 Cursor 这段任务指令：

> 请按本项目需求选择技能：UI 设计用 frontend-design；React/Next.js 用 react-best-practices；Bug 先 systematic-debugging，再 test-driven-development；UI 审查用 web-design-guidelines；浏览器测试用 webapp-testing。交付前执行 verification-before-completion，并报告实际运行结果。只有我要求分支交付时才使用 finishing-a-development-branch。不要一次性加载所有技能。

上游 Superpowers 文中有 `superpowers:test-driven-development` 等命名空间引用，在这份独立集合里映射到同名技能目录。它也可能引用未收录的技能，例如 using-git-worktrees；需要时明确报告缺少依赖，或另行安装完整 Superpowers，不能假装已经执行。原文保持不变。

## 运行依赖

- Skills 是指令和辅助文件，不会自动安装测试框架，也不是 MCP 服务。
- webapp-testing 使用 Python Playwright。按上游需要准备：`python3 -m pip install playwright`，然后 `python3 -m playwright install chromium`。先启动应用，或使用技能内的 with_server.py。
- web-design-guidelines 每次审查会联网读取 Vercel 的最新规则：<https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md>。离线时需要明确报告审查受限。
- React、单元测试和构建使用项目自己的工具与命令。本集合没有安装完整 Superpowers 插件或其钩子。
- 这些前端技能主要针对 Web；原生微信小程序需要补充 WXML/WXSS、微信 API、开发者工具等专用规则。

## 更新

`sources.lock.json` 记录三个上游仓库的完整 commit SHA，初始内容可复现。

```bash
# 从锁定版本重新同步
python3 scripts/sync.py
# 主动升级到上游最新版本
python3 scripts/sync.py --latest
git diff
# 检查改动、依赖和许可后，再 commit / push
```

同步会替换本仓库的 `skills/`，请先提交你的本地改动。它不会更新已经复制到 Cursor 的技能；备份旧安装目录后重新运行 install.py。这里采用手动升级，避免上游变化未经检查就进入你的开发工作流。

## 来源与许可证

详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。技能归各上游作者所有；本仓库只做汇集和安装辅助，未声称原创。各目录适用各自许可。
