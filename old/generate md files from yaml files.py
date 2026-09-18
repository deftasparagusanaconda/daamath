from pathlib import Path

pwd = Path()
files = list(pwd.iterdir())

for file in files:
    if file.suffix != '.yaml':
        continue

    md_file = Path(file.stem + '.md')
    
    if md_file in files:
        print(f"{md_file} already exists")
        continue

    md_file.write_text('\n'.join([
        '---',
        'hide:',
        '  - toc',
        '---',
        f'# {file.stem}',
        '',
        '{{ yaml_source(page) }}'
        ]))


    

