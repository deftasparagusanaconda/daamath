from pathlib import PurePosixPath


def define_env(env):
    @env.macro
    def yaml_source(page):
        markdown_path = PurePosixPath(page.path)
        yaml_path = 'yaml files/' + str(markdown_path.with_suffix(".yaml"))
        
        return (
            "# yaml\n\n"
            "```yaml\n"
            f'--8<-- "{yaml_path}"\n'
            "```"
        )
