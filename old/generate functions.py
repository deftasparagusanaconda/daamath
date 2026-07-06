# generate src/functions/*.py from specification/functions/*.yaml
#
# i wrote all this myself 😤
#
# proud of you, daa. proud of you.

from pathlib import Path
import yaml

FUNCTIONS = Path('../../../docs/specification/functions')
HANDWRITTEN = Path('../handwritten/daamath/')
SRC = Path('../src/daamath/')

def generate_definition(name: str, args: list[str], description: str) -> str:
    'generate a function definition'
    lines = [
        f'def {name}({', '.join(args)}):',
        f'    {description!r}']

    for arg in args:
        lines.append(f'    if not dm.context.{name}.domains.{arg}({arg}):')
        lines.append(f"        raise _DomainViolation('{name}', ({', '.join(args)}), {{}}, {arg}, dm.context.{name}.domains.{arg})")
    lines.append('')
    lines.append(f'    image = dm.context.{name}.graph({', '.join(args)})')
    lines.append('')
    lines.append(f'    if not dm.context.{name}.codomain(image):')
    lines.append(f"        raise _CodomainViolation('{name}', ({', '.join(args)}), {{}}, image, dm.context.{name}.codomain)")

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
        
    return 'import daamath as dm\nfrom ..exceptions import DomainViolation as _DomainViolation, CodomainViolation as _CodomainViolation\n\n' + '\n\n'.join(definitions) + '\n'

for path in FUNCTIONS.iterdir(): 
    if path.suffix != '.yaml':
        continue

    target = (SRC/'functions'/(path.stem+'.py'))

    print(f'hello! i am now generating {target}')
    
    target.write_text(generate_file(yaml.safe_load(path.read_text())))

print('generating functions/__init__.py')
(SRC/ 'functions' / '__init__.py').write_text('\n'.join(f'from .{path.stem} import *' for path in FUNCTIONS.iterdir() if path.suffix == '.yaml'))
