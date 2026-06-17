# generate signatures.yaml from functions/*.yaml

from pathlib import Path

FUNCTIONS = Path('functions/')

for path in FUNCTIONS.iterdir():
    if path.suffix != '.yaml':
        continue
    
    

