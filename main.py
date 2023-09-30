
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

    initial_content = "This is the initial content of your prompt file."
    user_prompt = get_user_prompt_file(initial_content=initial_content)
    
    print(user_prompt)

if __name__ == "__main__":
    main()
