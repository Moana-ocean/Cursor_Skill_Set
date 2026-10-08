#!/usr/bin/env python3
"""Build the categorized catalog from pinned source metadata."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
labels = {
    'ui': 'UI 设计与可访问性',
    'frontend': 'Web 前端、Vue 与 uni-app',
    'miniprogram': '微信小程序与开发者工具',
    'cloudbase': 'CloudBase 后端与云服务',
    'testing': '测试、调试、验收与交付',
    'review': '代码审查与安全',
    'monitoring': '线上错误与故障处理',
    'wordpress': 'WordPress 开发与运维',
}
groups = {key: [] for key in labels}
sources = {}
for source in json.loads((root / 'sources.lock.json').read_text())['sources']:
    repo = source['url'].removeprefix('https://github.com/').removesuffix('.git')
    for name in source['skills']:
        if repo.startswith('WordPress/'):
            category = 'wordpress'
        elif repo == 'getsentry/skills':
            category = 'review'
        elif repo == 'getsentry/sentry-agent-skills':
            category = 'monitoring'
        elif name in {'frontend-design', 'web-design-guidelines', 'ui-design'}:
            category = 'ui'
        elif repo.startswith('uni-helper/') or name == 'react-best-practices':
            category = 'frontend'
        elif name.startswith('miniapp-') or 'miniprogram' in name or name in {'ai-model-wechat', 'cloudbase-wechat-integration'}:
            category = 'miniprogram'
        elif repo.startswith('TencentCloudBase/'):
            category = 'cloudbase'
        else:
            category = 'testing'
        groups[category].append(name)
        sources[name] = repo
for names in groups.values():
    names.sort()
(root / 'categories.json').write_text(json.dumps(groups, ensure_ascii=False, indent=2) + '\n')
lines = ['# 技能目录', '', f'共 {len(sources)} 个独立技能，按用途选择。技能文件保留上游完整原文、参考文件和许可。', '']
for category, label in labels.items():
    lines.extend([f'## {label}', '', f'安装分类：`--category {category}`', '', '| 技能 | 来源 |', '| --- | --- |'])
    for name in groups[category]:
        repo = sources[name]
        lines.append(f'| [{name}](skills/{name}/SKILL.md) | [{repo}](https://github.com/{repo}) |')
    lines.append('')
(root / 'CATALOG.md').write_text('\n'.join(lines))
print(f'Catalog: {len(sources)} skills across {len(groups)} categories.')
