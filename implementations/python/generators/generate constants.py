# generate constants/*.py from specification/constants/*.yaml

from pathlib import Path
import yaml

SPECIFICATION = Path('../../../docs/specification/constants/')
CONSTANTS = Path('../src/daamath/constants/')

def yaml_dict_to_file(yaml_dict, *, indent=0, root=True) -> str:
    lines: list[str] = []

    for k, v in yaml_dict.items():
        pad = '  ' * indent

        if isinstance(v, dict):
            lines.append(f'{pad}{k} = _SimpleNamespace(')
            lines.append(yaml_dict_to_file(v, indent=indent + 1, root=False))
            lines.append(f'{pad}){"" if root else ","}')
        else:
            lines.append(f'{pad}{k} = {v!r}{"" if root else ","}')

    return '\n'.join(lines)

for path in SPECIFICATION.iterdir():
    if path.suffix != '.yaml':
        continue

    target = (CONSTANTS / (path.stem + '.py'))
    print(f'generating {target}')
    target.write_text('from types import SimpleNamespace as _SimpleNamespace\n\n' + yaml_dict_to_file(yaml.safe_load(path.read_text())))

(CONSTANTS / '__init__.py').write_text('\n'.join(f'from .{path.stem} import *' for path in SPECIFICATION.iterdir() if path.suffix == '.yaml'))
