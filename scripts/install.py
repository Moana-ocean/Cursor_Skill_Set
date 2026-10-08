#!/usr/bin/env python3
"""Copy curated skills to Cursor; never overwrite existing files."""
import argparse
import json
import shutil
from pathlib import Path

root = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
group = p.add_mutually_exclusive_group(required=True)
group.add_argument('--global', dest='global_install', action='store_true')
group.add_argument('--project', type=Path)
p.add_argument('--dry-run', action='store_true')
p.add_argument('--only', nargs='+', metavar='SKILL', help='Install only the named skill directories')
categories = json.loads((root / 'categories.json').read_text())
p.add_argument('--category', nargs='+', choices=list(categories), help='Install selected categories; may be combined with --only as an intersection')
a = p.parse_args()
target = Path.home() / '.cursor/skills' if a.global_install else a.project.resolve() / '.cursor/skills'
sources = sorted((root / 'skills').iterdir())
if a.category:
    selected = {name for category in a.category for name in categories[category]}
    sources = [s for s in sources if s.name in selected]
if a.only:
    unknown = set(a.only) - {s.name for s in sources}
    if unknown:
        p.error('Unknown skill names: ' + ', '.join(sorted(unknown)))
    sources = [s for s in sources if s.name in a.only]
if not sources or any(not (s / 'SKILL.md').is_file() for s in sources):
    p.error('Invalid source skill collection')
conflicts = [target / s.name for s in sources if (target / s.name).exists() or (target / s.name).is_symlink()]
tool_source = root / 'tools/wechat-gui-check'
tool_target = target.parent / 'tools/wechat-gui-check'
include_tool = any(s.name == 'miniapp-devtools-gui-check' for s in sources)
if include_tool and (tool_target.exists() or tool_target.is_symlink()):
    conflicts.append(tool_target)
if conflicts:
    p.error('Existing skills found; move them aside before installing: ' + ', '.join(map(str, conflicts)))
for source in sources:
    print(f'{source.name} -> {target / source.name}')
if include_tool:
    print(f'wechat-gui-check tools -> {tool_target}')
if not a.dry_run:
    target.mkdir(parents=True, exist_ok=True)
    for source in sources:
        shutil.copytree(source, target / source.name)
    if include_tool:
        tool_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(tool_source, tool_target)
    print(f'Installed {len(sources)} skills. Open a new Cursor Agent conversation to use them.')
