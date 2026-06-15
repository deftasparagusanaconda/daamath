from pathlib import Path
from colletions.abc import Mapping
import yaml

SOURCE = Path('source/')
SPECIFICATION = Path('../../docs/specification/')
GENERATED = Path('generated/')

def linesify(mapping: Mapping) -> list[str]:
    lines = []
    
    for k, v in mapping:
        if isinstance(v, Mapping):
            lines.extend(linesify(v))
        else:
            lines.append(f'{k}:{v}\n')
    
    return lines

# generate strings/*.py
for path in (SPECIFICATION / 'strings').iterdir():
    if path.suffix != '.yaml':
        continue

    with open(GENERATED / path.stem, 'w') as file:
        file.writelines(linesify(yaml.safeload(path)))

