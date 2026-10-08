# Cursor Skill Set

面向 Cursor 的开发技能工具箱：77 个技能，按用途分类。保留上游完整技能目录、参考文件、辅助脚本及许可证，按任务选择需要的技能。

## 分类导航

| 分类 | 安装标识 | 技能数 |
| --- | --- | ---: |
| UI 设计与可访问性 | `ui` | 3 |
| Web 前端、Vue 与 uni-app | `frontend` | 9 |
| 微信小程序与开发者工具 | `miniprogram` | 11 |
| CloudBase 后端与云服务 | `cloudbase` | 26 |
| 测试、调试、验收与交付 | `testing` | 5 |
| 代码审查与安全 | `review` | 3 |
| 线上错误与故障处理 | `monitoring` | 1 |
| WordPress 开发与运维 | `wordpress` | 19 |

查看 [完整技能目录](CATALOG.md)。`skills/` 使用扁平目录便于安装与跨技能引用；分类由 `categories.json` 管理，不区分收录时间。

## 安装到 Cursor

需要 Git 和 Python 3。在 Mac 终端运行：

```bash
git clone https://github.com/Moana-ocean/Cursor_Skill_Set.git
cd Cursor_Skill_Set
# 按分类安装，支持一次选多个分类
python3 scripts/install.py --global --category wordpress review monitoring
# 或只安装到指定项目
python3 scripts/install.py --project /Users/ocean/你的项目目录 --category miniprogram
# 或选择具体技能
python3 scripts/install.py --global --only uniapp uni-helper vue wp-rest-api
# 全量安装
python3 scripts/install.py --global
```

全局目录为 `~/.cursor/skills/`；项目目录为 `<项目>/.cursor/skills/`。加 `--dry-run` 可预览。安装复制完整目录，遇到同名文件夹会停止；先移走旧目录作为备份，或选择尚未安装的分类/技能。安装后打开新的 Cursor Agent 对话并检查技能发现情况。官方说明：<https://cursor.com/docs/skills>。

GUI 检查技能的配套工具会复制到 `.cursor/tools/wechat-gui-check`，保持上游相对路径有效。工具 README 中有关原仓库历史测试的 docs 链接请回源仓库查看。

## 按任务使用

| 任务 | 推荐入口与流程 |
| --- | --- |
| 设计或修改网页 | frontend-design；React 项目结合 react-best-practices；完成后做 web-design-guidelines 和 webapp-testing |
| 原生微信小程序 | miniprogram-development；脚手架用 miniapp-official-scaffold-alignment；开发者工具问题用 miniapp-devtools-cli-repair / recovery |
| uni-app 项目 | uni-app（目录名 uniapp）、uni-helper、vue、vue-best-practices；按需要加载 Pinia、Vite、UnoCSS 和 VueUse |
| CloudBase 后端 | 根据项目使用 cloud-functions、数据库、认证等对应技能；先确认实际云环境与授权 |
| WordPress 项目 | wordpress-router 选择流程，wp-project-triage 检查结构；插件用 wp-plugin-development，接口用 wp-rest-api，运维用 wp-wpcli-and-ops |
| WordPress 性能与检查 | wp-performance 排查慢请求；wp-phpstan 做静态分析；wp-env 或 wp-playground 复现问题 |
| 审查代码与安全 | code-review、find-bugs、security-review |
| Sentry 线上错误 | sentry-fix-issues，先连接 Sentry MCP 并确认目标组织/项目 |
| 修复与最终验收 | systematic-debugging → test-driven-development → verification-before-completion；需要分支交付时用 finishing-a-development-branch |

Agent 按需求加载技能；不要把全部技能一次性塞进上下文。上游 `superpowers:技能名` 引用映射到本仓库同名目录；未收录依赖应明确报告。WordPress 原文中的 `skills/...` 路径以本仓库根目录为基准，安装后对应 `.cursor/skills/...` 或 `~/.cursor/skills/...`，执行辅助脚本前先定位实际路径。

## 运行依赖与验证范围

- 技能是指令和辅助文件，不会自动安装工具或连接云账号、MCP 服务。
- webapp-testing 使用 Python Playwright：`python3 -m pip install playwright`，再运行 `python3 -m playwright install chromium`。
- web-design-guidelines 每次联网读取 Vercel 最新规范：<https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md>。
- CloudBase 操作需要腾讯云账号、正确环境，以及相应 MCP/CLI；安装技能不会部署云服务。
- 微信 GUI 检查需要本机微信开发者工具、Node.js 与 miniprogram-automator。
- WordPress 技能按任务需要 PHP、WP-CLI、Composer、Docker 或 Node.js 等，详见对应技能。
- sentry-fix-issues 需要配置 Sentry MCP 和项目访问权限；其余三个 Sentry 审查技能可从本地代码出发。
- 小程序集合部分技能标记为 draft/beta，uni-helper 上游标记为概念验证。来源说明保存在 `licenses/`。
- 本集合验证了文件保留、安装与同步流程，没有在真实 WordPress、小程序、Sentry 项目或云环境中运行全部技能。

## 更新与维护

```bash
git pull
# 根据锁定版本重建技能目录
python3 scripts/sync.py
# 主动升级已选技能到上游最新版本
python3 scripts/sync.py --latest
git diff
```

`sources.lock.json` 固定九个上游仓库的 commit SHA，并记录选取的技能、许可和配套文件。同步会替换本仓库 `skills/`，先提交你的本地改动；随后自动重建分类目录。分类生成脚本是 `scripts/catalog.py`。更新不会自动覆盖已复制到 Cursor 的技能；备份旧安装目录后重新安装。升级不会自动收录上游后来添加的新技能。

uni-helper 的 web-design-guidelines 与已收录 Vercel 版本完全一致，保留一份；去重记录在版本文件中。Sentry 开发集合选取 code-review、find-bugs、security-review，故障处理集合选取 sentry-fix-issues。WordPress 集合完整收录，供路由技能选择。

## 来源与许可证

详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。本仓库包含 Apache-2.0、MIT、GPL-2.0-or-later 等不同许可内容，Sentry 安全参考材料还保留 OWASP 的 CC-BY-SA-4.0 说明；各目录适用其自身条款。本仓库不声明这些上游技能为原创，也不以统一许可覆盖它们。
