import os

# # Use os.chdir to change the working directory, and os.mkdir to create a directory
# os.chdir(r"C:\Users\Arthur Djiomou\Github\ProjectMaker")
# os.mkdir("TestFolder")

# # Create a file. w+ is to create one if it isn't already existing
# test_file=open(r"TestFolder/test1.md", "w+")

def main():
    print("Welcome to Project Maker.")
    print("What type of project will it be?")
    print("1. Web project\n2. Godot Project")
    choice = int(input("Choice: "))

    match choice:
        case 1:
            CreateWebProject()

def CreateWebProject():
    project_name = input("What is the name of the project: ")
    dir = input("Please enter the directory for the project: ")
    os.chdir(dir)
    os.mkdir(project_name)

    html_file = open(f"{dir}\{project_name}\index.html", "w+")
    css_file = open(f"{dir}\{project_name}\style.css", "w+")
    js_file = open(f"{dir}\{project_name}\script.js", "w+")

    html_file.close()
    css_file.close()
    js_file.close()    

    print("Process Completed!")

main()