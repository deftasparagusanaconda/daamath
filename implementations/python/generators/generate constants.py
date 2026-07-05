# generate constants/*.py from specification/constants/*.yaml

from pathlib import Path
import yaml

SPECIFICATION = Path('../../../docs/specification/constants/')
CONSTANTS = Path('../src/daamath/constants/')

def yaml_dict_to_file(yaml_dict) -> str:
    lines: list[str] = ['from types import SimpleNamespace as _SimpleNamespace']
    
    for k, v in yaml_dict.items():
        lines.append(f'{k} = _SimpleNamespace(')

        if isinstance(v, dict):
            lines.append('  ' + yaml_dict_to_file(v))
        else:
            lines.append('  ' + repr(v))
    
    return '\n'.join(f'{k} = {v!r}' for k, v in yaml_dict.items())
    
    return '\n'.join(lines)

for path in SPECIFICATION.iterdir():
    if path.suffix != '.yaml':
        continue

    target = (CONSTANTS / (path.stem + '.py'))
    print(f'now generating {target}')
    
    target.write_text(yaml_dict_to_file(yaml.safe_load(path.read_text())))

(CONSTANTS / '__init__.py').write_text('\n'.join(f'from .{path.stem} import *' for path in SPECIFICATION.iterdir() if path.suffix == '.yaml'))
