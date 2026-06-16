# generate src/functions/*.py from specification/functions/*.yaml

from pathlib import Path
import yaml

SPECIFICATION = Path('../../../docs/specification/')
HANDWRITTEN = Path('../handwritten/daamath/')
SRC = Path('../src/daamath/')

def generate_definition(name: str, args: list[str], description: str) -> str:
    'generate a function definition'
    lines = [
        f'def {name}({', '.join(args)}):',
        f'    {description!r}']

    for arg in args:
        lines.append(f'    if not dm.context.{name}.domains.{arg}(arg):')
        lines.append(f'        raise DomainViolation({name}, {args}, arg)')

    lines.append(f'    image = dm.context.{name}.mapping({', '.join(args)})')

    lines.append(f'    if not dm.context.{name}.codomain(image):')
    lines.append(f'        raise CodomainViolation({name}, {args}, arg)')

    lines.append('\treturn image')

    return '\n'.join(lines)

def generate_file(yaml_dict) -> str:
    'convert function definitions from .yaml to .py'
    definitions = []

    for name, details in yaml_dict.items():
        description: str = details['description']
        args: list[str] = [list(d)[0] for d in details['domains']]
        
        definition = generate_definition(name, args, description)
        definitions.append(definition)
        
    return '\n'.join(definitions) + '\n'

for path in SPECIFICATION.iterdir(): 
    if path.suffix != '.yaml':
        continue
    
    (SRC/'functions'/path.stem/'.py').write_text(generate_file(yaml.safe_load(path.read_text())))
