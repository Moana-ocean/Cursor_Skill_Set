#!/usr/bin/env python3
"""Copy the eight curated skills to Cursor; never overwrite existing files."""
import argparse
import shutil
from pathlib import Path

root = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
group = p.add_mutually_exclusive_group(required=True)
group.add_argument('--global', dest='global_install', action='store_true')
group.add_argument('--project', type=Path)
p.add_argument('--dry-run', action='store_true')
a = p.parse_args()
target = Path.home() / '.cursor/skills' if a.global_install else a.project.resolve() / '.cursor/skills'
sources = sorted((root / 'skills').iterdir())
if not sources or any(not (s / 'SKILL.md').is_file() for s in sources):
    p.error('Invalid source skill collection')
conflicts = [target / s.name for s in sources if (target / s.name).exists() or (target / s.name).is_symlink()]
if conflicts:
    p.error('Existing skills found; move them aside before installing: ' + ', '.join(map(str, conflicts)))
for source in sources:
    print(f'{source.name} -> {target / source.name}')
if not a.dry_run:
    target.mkdir(parents=True, exist_ok=True)
    for source in sources:
        shutil.copytree(source, target / source.name)
    print('Installed 8 skills. Open a new Cursor Agent conversation to use them.')
