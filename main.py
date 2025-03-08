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

def main():
    print("Welcome to Project Maker.")
    print("Please make sure you have cd to the directory you want your project in.")
    print("What type of project will it be?")
    print("1. Web project\n2. Godot Project")
    choice = int(input("Choice: "))

    match choice:
        case 1:
            create_web()
        

def create_web():
    project_name = input("What is the name of the project: ")

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

    click.echo("Process Completed!")



main()