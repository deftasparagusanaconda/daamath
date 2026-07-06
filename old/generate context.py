# this file generates src/daamath/context.py

from pathlib import Path
import yaml

FUNCTIONS = Path('../../../docs/specification/functions')
CONTEXT = Path('../src/daamath/context.py')

INDENT: str = '    '

lines: list[str] = [
    'from . import domains as _domains, mappings as _mappings',
    'from .utils import Signature as _Signature',
    'from types import SimpleNamespace as _SimpleNamespace'
    '',
    'context = _SimpleNamespace(']

for path in FUNCTIONS.iterdir():
    if path.suffix != '.yaml':
        continue

    print('now generating context for', path)

    yaml_dict = yaml.safe_load(path.read_text())

    for func_name, signature in yaml_dict.items():
        domains = f','.join(f'\n{INDENT*3}{arg_name} = _domains.{domain}' for domain_dict in signature['domains'] for arg_name, domain in domain_dict.items())

        lines.append(f"""{INDENT}{func_name} = _Signature(
{INDENT*2}domains = _SimpleNamespace({domains}),
{INDENT*2}codomain = _domains.{signature['codomain']},
{INDENT*2}graphs = _graphs.{func_name}),\n""")

lines.append(')')
    
CONTEXT.write_text('\n'.join(lines))
