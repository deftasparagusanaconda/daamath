# generate signatures.yaml from functions/*.yaml
#
# the rule is that a function has only three things: 
# domain: a tuple of domains (as indicator functions)
# codomain: a domain (as indicator function)
# mapping: a set of tuples (as function)

import yaml
from pathlib import Path

FUNCTIONS = Path('functions/')
SIGNATURES = Path('signatures.yaml')

lines: list[str] = ['# signatures.yaml is a template for what daamath.signatures should look like']

for path in FUNCTIONS.iterdir():
    if path.suffix != '.yaml':
        continue
    
    lines.append(f'{path.stem}:')
    yaml_dict = yaml.safe_load(path.read_text())
    
    for func_name, details in yaml_dict.items():
        lines.append(f'  {func_name}:')
        # python's dict remembers insertion order
        domains: dict[str, str] = {k: v for domains_dict in details['domains'] for k, v in domains_dict.items()}

        lines.append('    domains:')
        for argument_name, domain in domains.items():
            lines.append(f'      - {argument_name}: {domain}')
        
        lines.append(f"    codomain: {details['codomain']}")
        lines.append("    mapping: your programming language's function here")
    
SIGNATURES.write_text('\n'.join(lines) + '\n')
