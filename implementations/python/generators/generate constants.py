# generate constants/*.py from specification/constants/*.yaml

from pathlib import Path
import yaml

SPECIFICATION = Path('../../../docs/specification/constants/')
CONSTANTS = Path('../src/daamath/constants/')

def yaml_dict_to_file(yaml_dict):
    return '\n'.join(f'{k} = 0x{v:x}'if isinstance(v, int) else f'{k} = {v!r}' for k, v in yaml_dict.items())

for path in SPECIFICATION.iterdir():
    if path.suffix != '.yaml':
        continue

    target = (CONSTANTS / (path.stem + '.py'))
    print(f'now generating {target}')

    yaml_dict = yaml.safe_load(path.read_text())

    target.write_text(yaml_dict_to_file(yaml.safe_load(path.read_text())))

(CONSTANTS / '__init__.py').write_text('\n'.join(f'from .{path.stem} import *' for path in SPECIFICATION.iterdir() if path.suffix == '.yaml'))
