# this file generates src/daamath/context/signatures.py

from pathlib import Path
import yaml

FUNCTIONS = Path('../../../docs/specification/functions')
SIGNATURES = Path('../src/daamath/context/signatures.py')

INDENT: str = '    '

lines: list[str] = [
    'from .. import domains, mappings',
    'from ..utils import Namespace, Signature\n']

for path in FUNCTIONS.iterdir():
    if path.suffix != '.yaml':
        continue

    print('now generating signatures for', path)

    yaml_dict = yaml.safe_load(path.read_text())

    for func_name, signature in yaml_dict.items():
        domains = f','.join(f'\n{INDENT*2}{arg_name}=domains.{domain}' for domain_dict in signature['domains'] for arg_name, domain in domain_dict.items())

        lines.append(f"""{func_name} = Signature(
{INDENT}domains=Namespace({domains}),
{INDENT}codomain=domains.{signature['codomain']},
{INDENT}mapping=mappings.{func_name})\n""")
    
SIGNATURES.write_text('\n'.join(lines))
