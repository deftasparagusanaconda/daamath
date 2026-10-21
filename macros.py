import pathlib, yaml
#from itertools import batched

def define_env(env):
    @env.macro
    def yaml_source(page):
        markdown_path = pathlib.PurePosixPath(page.path)
        yaml_path = 'yaml files/' + str(markdown_path.with_suffix(".yaml"))
        
        return (
            '<details><summary><h1 id="yaml">yaml</h1></summary>\n\n'
            "```yaml\n"
            f'--8<-- "{yaml_path}"\n'
            "```\n\n"
            "</details>"
        )
    
    @env.macro
    def math_constants():
        from decimal import Decimal, Context, ROUND_DOWN

        ctx = Context(prec=12, rounding=ROUND_DOWN)

        lines = []

        for idk in yaml.safe_load(open('yaml files/constants/index.yaml')):
            name = f"[`{idk['name']}`]({idk['name']})" 

            eponyms = '<br>'.join(
                f"[{''.join(flag + ' ' for flag in idfk['flags']) + idfk['name']}]({idfk['link']})" 
                if idfk['link'] is not None
                else ''.join(flag + ' ' for flag in idfk['flags']) + idfk['name']
                for idfk in idk['eponyms'])

            formula = (
                f"{idk['formula']}" 
                if idk['formula'] is not None 
                else '')

            try:
                digs = str(ctx.create_decimal((pathlib.Path("constant decimals") / f"{idk['name']}.txt").read_text().strip()))
            except Exception as e:
                digs = str(e)
            #digs = '<br>'.join(''.join(tup) for tup in batched(idk['decimal'], 120))
            decimal = (
                f"[{digs}]({idk['oeis']})" 
                if idk['oeis'] is not None 
                else digs)
            
            notes = (
                idk['notes']
                if idk['notes'] is not None
                else '')
            
            
            lines.append(f"| {name} | {eponyms} | {formula} | {decimal} | {notes} |")

        return '\n'.join(lines)
