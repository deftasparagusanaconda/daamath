import sys, yaml

for idk in yaml.safe_load(sys.stdin.read()):
    name = (
        f"[`{idk['name']}`]({idk['link']})" 
        if idk['link'] is not None 
        else f"`{idk['name']}`")

    eponyms = ', '.join(
        f"[{idfk['name']}]({idfk['link']})" 
        if idfk['link'] is not None
        else idfk['name']
        for idfk in idk['eponyms'])

    formula = (
        f"{idk['formula']}" 
        if idk['formula'] is not None 
        else '')
    
    decimal = (
        f"[{idk['decimal']}]({idk['oeis']})" 
        if idk['oeis'] is not None 
        else idk['decimal'])
    
    sys.stdout.write(f"| {name} | {eponyms} | {formula} | {decimal} |\n")
