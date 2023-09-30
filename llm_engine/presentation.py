from diagrams import Diagram
import subprocess
import os

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
        # The file already exists, you can choose how to handle this case
        pass


def generate_diagram_from_code(diagram_code):
    """
    Generate a diagram from Python code and execute it as a separate process.
    Args:
        diagram_code (str): Python code representing the diagram.
    """
    folder_path = 'llm_engine/assets'
    file_name = 'generated_diagram_code.py'

    create_folder_and_file(folder_path, file_name, diagram_code)
    
    # Full path to the script
    script_path = os.path.join(folder_path, file_name)

    # Run the script as a separate process.
    process = subprocess.Popen(['python', script_path], stderr=subprocess.PIPE)
    stderr = process.communicate()

    if process.returncode == 0:
        print("Diagram successfully generated.")
    else:
        print("Error while generating the diagram:")
        print(stderr.decode('utf-8'))


        
