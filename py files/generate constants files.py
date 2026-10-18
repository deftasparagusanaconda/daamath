from daamath import binary32, binary64, binary128, decimal64, decimal128
from typing import Any

formats = [binary32, binary64, binary128, decimal64, decimal128]

def generate page(yaml: dict[str, Any], decimal: str):
    # reps[format: type][representation: ] = 
    reps = dict.fromkeys(formats)
    for format in formats:
    
    return '''# {yaml['name']}
