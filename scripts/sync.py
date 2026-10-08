#!/usr/bin/env python3
"""Rebuild vendored skills from pinned upstream commits; --latest updates pins."""
import argparse
import json
import shutil
import subprocess
import tempfile
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--latest', action='store_true', help='Fetch upstream HEAD and update sources.lock.json; review diffs before committing')
a = p.parse_args()
lock = json.loads((root / 'sources.lock.json').read_text())
def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()
with tempfile.TemporaryDirectory() as temp:
    work = Path(temp)
    staged = work / 'skills'
    staged.mkdir()
    staged_licenses = work / 'licenses'
    staged_licenses.mkdir()
    staged_tools = work / 'tools'
    staged_tools.mkdir()
    for i, source in enumerate(lock['sources']):
        checkout = work / str(i)
        git('clone', '--quiet', '--no-checkout', source['url'], str(checkout))
        ref = 'origin/HEAD' if a.latest else source['commit']
        git('-C', str(checkout), 'checkout', '--quiet', '--detach', ref)
        source['commit'] = git('-C', str(checkout), 'rev-parse', 'HEAD')
        for name in source['skills']:
            original = checkout / 'skills' / name
            if not (original / 'SKILL.md').is_file():
                raise RuntimeError(f'Missing upstream skill: {name}')
            shutil.copytree(original, staged / name)
            if source['license_file']:
                destination = staged / name / 'LICENSE.txt'
                if destination.exists():
                    destination = staged / name / 'UPSTREAM-LICENSE.txt'
                shutil.copy2(checkout / source['license_file'], destination)
            if source.get('license_template'):
                shutil.copy2(root / source['license_template'], staged / name / 'LICENSE.txt')
            if source.get('license_text_template'):
                shutil.copy2(root / source['license_text_template'], staged / name / 'COPYING.txt')
        for original, destination in source.get('extra_files', {}).items():
            shutil.copy2(checkout / original, staged_licenses / destination)
        for original, destination in source.get('extra_directories', {}).items():
            relative = Path(destination).relative_to('tools')
            shutil.copytree(checkout / original, staged_tools / relative)
    # Only replace after every upstream download succeeded. Track local edits in Git first.
    if (root / 'skills').exists():
        shutil.rmtree(root / 'skills')
    shutil.copytree(staged, root / 'skills')
    (root / 'licenses').mkdir(exist_ok=True)
    for original in staged_licenses.iterdir():
        shutil.copy2(original, root / 'licenses' / original.name)
    for original in staged_tools.iterdir():
        destination = root / 'tools' / original.name
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(original, destination)
    if a.latest:
        (root / 'sources.lock.json').write_text(json.dumps(lock, ensure_ascii=False, indent=2) + '\n')
    print(f'Synced {len(list(staged.iterdir()))} complete skill directories. Review git diff before committing.')
subprocess.run([sys.executable, str(root / 'scripts/catalog.py')], check=True)
