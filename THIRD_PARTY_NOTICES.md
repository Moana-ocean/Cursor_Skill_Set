# Third-party notices

The vendored skill files retain their upstream contents. Root upstream MIT license notices are copied into imported skill directories. Existing per-skill licenses remain intact; if LICENSE.txt already exists, the root notice is added as UPSTREAM-LICENSE.txt.

- Anthropic: https://github.com/anthropics/skills — frontend-design and webapp-testing; Apache License 2.0. Each directory includes its original LICENSE.txt. Original notices remain intact.
- Vercel Labs: https://github.com/vercel-labs/agent-skills — web-design-guidelines and react-best-practices. The upstream root README declares MIT; React SKILL.md also declares MIT. No standalone root LICENSE was present in the pinned snapshot. The original README is preserved in licenses/vercel-upstream-README.md as evidence; this collection does not invent an upstream copyright notice or replacement license text.
- Jesse Vincent / Superpowers: https://github.com/obra/superpowers — test-driven-development, systematic-debugging, verification-before-completion, finishing-a-development-branch; MIT. The original root license, including its copyright notice, is copied into each imported directory.

Exact source commits are recorded in sources.lock.json. Repository documentation and installation/synchronization helpers are collection-specific additions. Consult upstream terms for redistribution and modification of the imported materials.

- Tencent CloudBase: https://github.com/TencentCloudBase/skills — 32 skills, MIT; Copyright (c) 2025 Tencent CloudBase. Root license and README are preserved under licenses/.
- Sun-sunshine06: https://github.com/Sun-sunshine06/miniprogram-skills — 6 skills and tools/wechat-gui-check, MIT; Copyright (c) 2026 Contributors. Root license and README are preserved under licenses/.
- uni-helper: https://github.com/uni-helper/skills — 8 additional skills, MIT; Copyright (c) 2026 FliPPeDround. Original per-skill licenses and credits (including external Vue/VueUse/antfu sources) remain intact. Root license and README are preserved under licenses/. Its web-design-guidelines duplicate is omitted; the identical Vercel version remains in this collection.

- Sentry development skills: https://github.com/getsentry/skills — code-review, find-bugs, security-review; root Apache-2.0 license preserved. The security-review/LICENSE notice attributes its reference materials to OWASP under CC-BY-SA-4.0; its original notice and all references remain unchanged. The added LICENSE.txt is the repository's separate Apache-2.0 notice, not a replacement of the OWASP terms.
- Sentry issue remediation: https://github.com/getsentry/sentry-agent-skills — sentry-fix-issues. Apache-2.0 is declared in its original frontmatter and upstream README; no root LICENSE file was present in the pinned snapshot. An unmodified standard Apache-2.0 license text is included as LICENSE.txt without inventing a Sentry copyright notice.
- WordPress contributors: https://github.com/WordPress/agent-skills — complete 19-skill collection; GPL-2.0-or-later. The original root notice is preserved as LICENSE.txt in every skill; COPYING.txt supplies the unmodified GPL v2 license text. Root notice, README and full terms are retained under licenses/.
