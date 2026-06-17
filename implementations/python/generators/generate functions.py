# generate src/functions/*.py from specification/functions/*.yaml
#
# i wrote all this myself 😤
#
# proud of you, daa. proud of you.

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
        lines.append(f"        raise DomainViolation('{name}', {args}, {{}}, arg, dm.context.{name}.domains.{arg})")

    lines.append(f'    image = dm.context.{name}.mapping({', '.join(args)})')

    lines.append(f'    if not dm.context.{name}.codomain(image):')
    lines.append(f"        raise CodomainViolation('{name}', {args}, {{}}, image, dm.context.{name}.codomain)")

    lines.append('    return image')

    return '\n'.join(lines)

def generate_file(yaml_dict) -> str:
    'convert function definitions from a .yaml to a .py'
    definitions = []

    for name, details in yaml_dict.items():
        description: str = details['description']
        args: list[str] = [list(d)[0] for d in details['domains']]
        
        definition = generate_definition(name, args, description)
        definitions.append(definition)
        
    return 'import daamath as dm\nfrom ..exceptions import DomainViolation, CodomainViolation\n\n' + '\n\n'.join(definitions) + '\n'

for path in (SPECIFICATION/'functions').iterdir(): 
    if path.suffix != '.yaml':
        continue

    target = (SRC/'functions'/(path.stem+'.py'))

    print(f'hello! i am now generating {target}')
    
    target.write_text(generate_file(yaml.safe_load(path.read_text())))
