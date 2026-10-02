import pathlib, yaml

def define_env(env):
    @env.macro
    def yaml_source(page):
        markdown_path = pathlib.PurePosixPath(page.path)
        yaml_path = 'yaml files/' + str(markdown_path.with_suffix(".yaml"))
        
        return (
            "# yaml\n\n"
            "```yaml\n"
            f'--8<-- "{yaml_path}"\n'
            "```"
        )
    
    @env.macro
    def math_constants():
        lines = []

        for idk in yaml.safe_load(open('yaml files/constants/math.yaml')):
            name = (
                f"[`{idk['name']}`]({idk['link']})" 
                if idk['link'] is not None 
                else f"`{idk['name']}`")

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
            
            lines.append(f"| {name} | {eponyms} | {formula} | {decimal} |")

        return '\n'.join(lines)
