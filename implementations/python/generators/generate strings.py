# generate strings/*.py

# jsyk i made ai generate the to_python function so if theres nonsense there, you know why

import yaml
from pathlib import Path
from collections.abc import Mapping

# do you know why i keep putting lots of comments everywhere?
# its probably because ive stopped understanding what im doing

HANDWRITTEN = Path('../handwritten/daamath')
SPECIFICATION = Path('../../../docs/specification/')
SRC = Path('../src/daamath')
SRC_STRINGS = SRC / 'strings/'

# what indentation scheme youre using. by PEP rules, four spaces should be best
INDENT = '    '

# now from this point on, daa, you start generating your own code
# this is where youre dreading the most. come on, you can do it!
# first we have to take the strings/*.yaml and turn each file into its corresponding .py file. you better let a function do that. you should have a function that takes in a dict, and gives you back a string fit for a .py file. okie?
# okay... i-i guess i could do that
# good. go on.. go make it. lets see what happens
# ill make a function called.. dict_to_str.. i guess??

def to_python(obj, depth=0):
    indent = INDENT * depth
    next_indent = INDENT * (depth + 1)

    if isinstance(obj, Mapping):
        if not obj:
            return "_SimpleNamespace()"

        body = ",\n".join(
            f'{next_indent}{key} = {to_python(value, depth + 1)}'
            for key, value in obj.items()
        )

        # im going insane
        # do you know why i make a dict and then unpack it?
        # ill tell you why
        # because strings/greek.yaml has "lambda" which python thinks is a lambda. so im sidestepping all of that

        return (
            "_SimpleNamespace(\n"
            f"{body}\n"
            f"{indent})"
        )

    if isinstance(obj, list):
        if not obj:
            return "[]"

        body = ",\n".join(
            f"{next_indent}{to_python(item, depth + 1)}"
            for item in obj
        )

        return (
            "[\n"
            f"{body}\n"
            f"{indent}]"
        )

    return repr(obj)

# mkdir src/strings/
SRC_STRINGS.mkdir(parents = True, exist_ok = True)

# create src/strings/*.py
for path in (SPECIFICATION / "strings").iterdir():
    if path.suffix != ".yaml":
        continue

    data = yaml.safe_load(path.read_text())

    code = ["from types import SimpleNamespace as _SimpleNamespace\n\n"]

    for variable, dictionary in data.items():
        code.append(f'{variable} = {to_python(dictionary)}\n')

    target = (SRC_STRINGS / f"{path.stem}.py")

    print(f'hello! i am now generating {target}')
    target.write_text(''.join(code))

# create src/strings/__init__.py

(SRC_STRINGS / '__init__.py').write_text('\n'.join(f'from .{path.stem} import *' for path in SRC_STRINGS.iterdir()))
