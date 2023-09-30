from llm_engine.openai_integration import *
from llm_engine.config import get_openai_api_key

def get_user_prompt_file(file_name='prompt', initial_content=None):
    try:
        with open(file_name, 'r') as file:
            user_prompt = file.read()
    except FileNotFoundError:
        with open(file_name, 'w') as file:
            if initial_content is not None:
                file.write(initial_content)
            user_prompt = "A new file has been created for you. You can start creating your own cloud diagram here."
    
    return user_prompt


def main():

    openai_api_key, error_message = get_openai_api_key()

    if error_message is not None:
        print(f"Error: {error_message}")
        exit
    
    initial_content = "This is the initial content of your prompt file."
    user_prompt = get_user_prompt_file(initial_content=initial_content)
    
    try:
        # Generate Python code for diagrams from the user prompt
        diagram_code = generate_code(user_prompt, openai_api_key)
        print(diagram_code)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()



