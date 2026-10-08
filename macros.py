import pathlib, yaml

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
        lines = []

        for idk in yaml.safe_load(open('yaml files/constants/index.yaml')):
            name = f"[`{idk['name']}`]({idk['name']})" 

            eponyms = '<br>'.join(
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
            
            notes = (
                idk['notes']
                if idk['notes'] is not None
                else '')
                
            
            lines.append(f"| {name} | {eponyms} | {formula} | {decimal} | {notes} |")

        return '\n'.join(lines)
