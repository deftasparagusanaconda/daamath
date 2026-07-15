from pathlib import Path

Path('../../src/daamath/constants/__init__.py').write_text('from . import *\n\n' + 
    '\n'.join(
        f'from .{file.stem} import *' 
        for file 
        in Path('../../../../docs/specification/constants/').iterdir()
        if file.suffix == '.yaml'))
