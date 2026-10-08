#!/usr/bin/env python3
"""Rebuild vendored skills from pinned upstream commits; --latest updates pins."""
import argparse
import json
import shutil
import subprocess
import tempfile
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
                shutil.copy2(checkout / source['license_file'], staged / name / 'LICENSE.txt')
    # Only replace after every upstream download succeeded. Track local edits in Git first.
    if (root / 'skills').exists():
        shutil.rmtree(root / 'skills')
    shutil.copytree(staged, root / 'skills')
    if a.latest:
        (root / 'sources.lock.json').write_text(json.dumps(lock, ensure_ascii=False, indent=2) + '\n')
    print('Synced 8 complete skill directories. Review git diff before committing.')
