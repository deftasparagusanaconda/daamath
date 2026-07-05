# generate 'context template.yaml'

# im not sure how to go about this yet. 
# the thing is... i dont know what the hierarchy should look like. 
# 
# context is a struct, and its structure has to be generated. then for contexts (instances of context), we need to copy the context struct and edit it by hand. this is all in official spec, btw. not in implementation
#
# then on *top* of that, implementation has to generate its source files for the context struct and for the contexts.
#
# so first of all, we need a .py file that can generate context.yaml, which describes the Context struct
#
# then we shall copy the structure to contexts/*.yaml and edit by hand how we want there, describing the contexts we want.

# okay. then it is decided. this file will generate that first 'context template.yaml'

from yaml import safe_load
from pathlib import Path

FUNCTIONS = Path('functions/')

lines = []

for dir in FUNCTIONS.iterdir():
    if dir.suffix != '.yaml':
        continue

    print('now working on', dir.stem)
    
    for func_name, details in safe_load(dir.read_text()).items():
        lines.append('\n# ' + ' '.join(details['signatures'].keys()))
        lines.append(func_name + ':')

Path('context template.yaml').write_text('\n'.join(lines))
