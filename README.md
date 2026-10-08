# Coding Skills — Cursor 开发技能工具箱

汇集 54 个上游技能，用于 UI 设计、React/Next.js、测试、调试、验收和分支交付。保留上游完整目录与原文，不把八份指令合并进一个大提示词；Agent 按任务加载需要的技能。

完整的 54 个技能见 [CATALOG.md](CATALOG.md)。

## 原有技能导航

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

## 新增：微信小程序、CloudBase 与 uni-app

| 来源 | 新增技能 | 用途 |
| --- | ---: | --- |
| [TencentCloudBase/skills](https://github.com/TencentCloudBase/skills) | 32 | 小程序开发、登录、数据库、云函数、云托管和 AI 模型集成 |
| [Sun-sunshine06/miniprogram-skills](https://github.com/Sun-sunshine06/miniprogram-skills) | 6 | 官方脚手架、开发者工具修复、GUI 检查、导航重构和文案 |
| [uni-helper/skills](https://github.com/uni-helper/skills) | 8 | uni-app、uni-helper、Vue、Pinia、Vite、UnoCSS 和 VueUse |

保留原来的 8 个技能，总计 54 个。uni-helper 的 web-design-guidelines 与已收录的 Vercel 版本完全相同，保留 Vercel 来源的一份，去重记录在 sources.lock.json。

小程序技能有部分标记为 draft/beta；uni-helper 上游说明这是尚未充分实测的概念验证集合。具体状态保留在上游说明中。GUI 检查需本机微信开发者工具、Node.js 和 miniprogram-automator；本次只验证文件与安装流程，没有运行真实小程序或云服务。

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

全局位置是 `~/.cursor/skills/`；项目位置是 `<项目>/.cursor/skills/`。安装会复制每个技能的完整目录。遇到同名目录会停止，不覆盖你的内容；先把旧目录移到备份位置，再重新安装。可以加 `--dry-run` 预览安装位置；用 `--only` 只安装指定技能。安装后打开新的 Cursor Agent 对话，并检查技能是否被发现。官方说明：<https://cursor.com/docs/skills>。

若使用本次提供的 Git bundle，可以直接把 bundle 当作 Git 仓库 clone：

```bash
git clone /下载路径/coding-skills.bundle coding-skills
cd coding-skills
python3 scripts/install.py --global
```

只安装小程序常用技能：

```bash
python3 scripts/install.py --global --only miniprogram-development auth-wechat-miniprogram miniapp-official-scaffold-alignment miniapp-devtools-cli-repair miniapp-devtools-gui-check
```

只安装 uni-app 常用技能（目录名称为 `uniapp`，上游技能名称为 `uni-app`）：

```bash
python3 scripts/install.py --global --only uniapp uni-helper vue vue-best-practices pinia vite unocss vueuse-functions
```

如果你已安装原来的 8 个技能，用 `--only` 选新增技能即可；不要直接全量安装到包含同名目录的位置。GUI 检查技能的配套工具会安装在 `.cursor/tools/wechat-gui-check`，保持上游相对路径有效。工具 README 中有关原仓库历史测试的 docs 链接请回源仓库查看。

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
- 微信小程序相关技能已加入；按项目选择原生小程序、CloudBase 或 uni-app 路线。CloudBase 技能中的云端操作需要配置对应账号、环境及 MCP/CLI；安装技能本身不会自动连接腾讯云。

## 更新

`sources.lock.json` 记录六个上游仓库的完整 commit SHA，初始内容可复现。

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
