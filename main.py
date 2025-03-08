import os
import click
import yaml


with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# # Use os.chdir to change the working directory, and os.mkdir to create a directory
# os.chdir(r"C:\Users\Arthur Djiomou\Github\ProjectMaker")
# os.mkdir("TestFolder")

# # Create a file. w+ is to create one if it isn't already existing
# test_file=open(r"TestFolder/test1.md", "w+")

@click.group()
def cli():
    """ProjectMaker CLI Tool"""
    pass

@click.command()
@click.argument("project_name")
def create_web(project_name):
    """Creates a basic Web Project"""

    project_path = os.path.join(os.getcwd(), project_name)
    
    # Make sure to control which directory to use
    if not os.path.exists(project_path):
        os.makedirs(project_path)
    else:
        click.echo("Directory already exists.")
        return    

    for file in config["project_templates"]["web"]["files"]:
        file_path = os.path.join(project_path, file)

        with open(file_path, "w+") as f:
            if file == "index.html":
                html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    
    <script src="script.js"></script>
</body>
</html>"""

                f.write(html_template)
            elif file == "README.md":
                f.write(f"{project_name} - Web Project")

            f.close()

    click.echo(f"Web project '{project_name}' created successfully.")


@click.command()
@click.argument("project_name")
def create_godot(project_name):
    """Creates a Godot 4.4 Project"""

    project_path = os.path.join(os.getcwd(), project_name)
    
    # Make sure to control which directory to use
    if not os.path.exists(project_path):
        os.makedirs(project_path)
    else:
        click.echo("Directory already exists.")
        return 
    
    for folder in config["project_templates"]["godot"]["folders"]:
        folder_path = os.path.join(project_path, folder)
        os.makedirs(folder_path)
    
    for file in config["project_templates"]["godot"]["files"]:
        file_path = os.path.join(project_path, file)
        with open(file_path, "w+") as f:
            if file == "project.godot":
                godot_template = f"""; Engine configuration file.
; It's best edited using the editor UI and not directly,
; since the parameters that go here are not all obvious.
;
; Format:
;   [section] ; section goes between []
;   param=value ; assign values to parameters

config_version=5

[application]

config/name="{project_name}"
config/features=PackedStringArray("4.4", "Forward Plus")
config/icon="res://icon.svg"

[rendering]

renderer/rendering_method="forward_plus"
"""

                f.write(godot_template)
            elif file == "README.md":
                f.write(f"{project_name} - Godot Project")
            elif file == ".gitatttributes":
                f.write("""# Normalize EOL for all files that Git considers text files.\n* text=auto eol=lf""")
            elif file == ".gitignore":
                f.write("# Godot 4+ specific ignores\n.godot/\n/android/")

            f.close()

    click.echo(f"Godot project '{project_name}' created successfully.")

def create_unity(project_name):
    """Creates a Unity Project"""

    project_path = os.path.join(os.getcwd(), project_name)
    
    # Make sure to control which directory to use
    if not os.path.exists(project_path):
        os.makedirs(project_path)
    else:
        click.echo("Directory already exists.")
        return 
    
    for folder in config["project_templates"]["unity"]["folders"]:
        folder_path = os.path.join(project_path, folder)
        os.makedirs(folder_path)
    
    for file in config["project_templates"]["unity"]["files"]:
        file_path = os.path.join(project_path, file)
        with open(file_path, "w+") as f:
            if file == "README.md":
                f.write(f"{project_name} - Unity Project")
            if file == ".gitignore":
                unity_gitignore = """  
[Ll]ibrary/  
[Tt]emp/  
[Oo]bj/  
[Bb]uild/  
[Bb]uilds/  
[Ll]ogs/  
UserSettings/  
*.csproj  
*.unityproj  
*.sln  
*.suo  
*.tmp  
*.user  
*.userprefs  
*.pidb  
*.booproj  
"""
                f.write(unity_gitignore)
    
    click.echo(f"Unity project '{project_name}' created successfully.")

cli.add_command(create_web)
cli.add_command(create_godot)
cli.add_command(create_unity)

if __name__ == "__main__":
    cli()