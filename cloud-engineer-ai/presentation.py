from diagrams import Diagram
import subprocess
import os
import shutil
import re

def create_folder_and_file(folder_path, file_name, content):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, file_name)

    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(content)
    else:
        with open(file_path, 'w') as f:
            f.write(content)

def create_folder(folder_path):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def generate_diagram_from_code(diagram_code):
    """
    Generate a diagram from Python code and execute it as a separate process.
    Args:
        diagram_code (str): Python code representing the diagram.
    """
    folder_path = '../project/output'
    file_name = 'generated_diagram_code.py'

    create_folder_and_file(folder_path, file_name, diagram_code)
    image_name = fetch_image_name(diagram_code)

    # Full path to the script
    script_path = os.path.join(folder_path, file_name)

    # Run the script as a separate process.
    process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        move_generate_image(image_name)
        print("Diagram successfully generated.")
    else:
        print("Error while generating the diagram:")
        print(stderr.decode('utf-8'))


def move_generate_image(image_name):
    
    folder_path = '../project/output/'

    create_folder(folder_path)

    source_path = image_name + ".png"

    # Define the target folder where you want to move the image
    target_path = folder_path+image_name+".png"

    # Move the file to the target folder
    shutil.move(source_path, target_path)

def fetch_image_name(diagram_code):

    # Define a regular expression pattern to match the Diagram("Mail Service") line
    pattern = r'with Diagram\("(.+?)"'

    # Use re.search to find the match in the code
    match = re.search(pattern, diagram_code)
    
    if match:
        image_name = match.group(1)
    else:
        image_name = "cloud.png"

    image_name = image_name.lower()

    image_name = f"{image_name.replace(' ', '_')}"
    
    return image_name

def generate_file_from_code(terraform_code):
    folder_path = '../project/output'
    file_name = 'terraform.tf'

    create_folder_and_file(folder_path, file_name, terraform_code)

        
