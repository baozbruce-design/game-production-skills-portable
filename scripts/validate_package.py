"""Validate the portable snapshot without running providers or installing skills."""
from pathlib import Path
import ast
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def main():
    errors = []
    tracked = set()
    for line in (ROOT / 'MANIFEST-SHA256.txt').read_text(encoding='utf-8-sig').splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r'([A-Fa-f0-9]{64})  (.+)', line)
        if not match:
            errors.append('Malformed manifest line')
            continue
        digest, name = match.groups()
        path = (ROOT / name.replace('\\', '/')).resolve()
        if not path.is_relative_to(ROOT) or name in tracked:
            errors.append('Invalid manifest path: ' + name)
            continue
        tracked.add(name)
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest.lower():
            errors.append('Hash mismatch: ' + name)
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()
              and not set(p.relative_to(ROOT).parts) & {'.git','__pycache__','.venv','dist'}
              and p.name != 'MANIFEST-SHA256.txt'}
    if actual != tracked:
        errors.append('Manifest file-set mismatch: ' + str(sorted(actual ^ tracked)))
    skills = sorted((ROOT / 'skills').glob('*/SKILL.md'))
    if len(skills) != 83:
        errors.append(f'Expected 83 skills, found {len(skills)}')
    for path in skills:
        text = path.read_text(encoding='utf-8-sig')
        match = re.match(r'---\s*\n(.*?)\n---', text, re.S)
        if not match:
            errors.append('Missing frontmatter: ' + path.parent.name)
            continue
        front = match[1]
        if not re.search(r'^name:\s*' + re.escape(path.parent.name) + r'\s*$', front, re.M):
            errors.append('Skill name mismatch: ' + path.parent.name)
        if not re.search(r'^description:\s*\S', front, re.M):
            errors.append('Missing description: ' + path.parent.name)
    for path in ROOT.rglob('*.py'):
        if '.git' in path.parts:
            continue
        try:
            ast.parse(path.read_text(encoding='utf-8-sig'), filename=str(path))
        except SyntaxError as exc:
            errors.append(f'Python syntax: {path.relative_to(ROOT)}:{exc.lineno}')
    for path in (ROOT / 'skills/router').rglob('*.md'):
        text = path.read_text(encoding='utf-8-sig')
        if re.search(r'skills/(godot|unity|unreal|other-engines|web-engines|disciplines|genres|workflows)/', text):
            errors.append('Nonportable router path: ' + str(path.relative_to(ROOT)))
        if re.search(r'\.\./(?:\.\./)?docs/', text):
            errors.append('Missing external router docs: ' + str(path.relative_to(ROOT)))
    secret_patterns = [r'ghp_[A-Za-z0-9]{30,}', r'github_pat_[A-Za-z0-9_]{40,}',
                       r'AIza[A-Za-z0-9_-]{35}', r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
    for name in actual:
        path = ROOT / name
        if path.suffix in {'.md','.py','.json','.yaml','.yml','.ps1','.mjs','.js','.txt'}:
            text = path.read_text(encoding='utf-8-sig')
            if any(re.search(pattern, text) for pattern in secret_patterns):
                errors.append('Potential credential in: ' + name)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(tracked)} files, {len(skills)} skills; hashes, metadata, Python syntax, router paths and credential patterns checked.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
