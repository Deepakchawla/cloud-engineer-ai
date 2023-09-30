import os

def get_openai_api_key():
    try:
        openai_api_key = os.getenv('OPENAI_API_KEY')
        if openai_api_key is None:
            raise ValueError("OPENAI_API_KEY environment variable is not set.")
    except ValueError as e:
        return None, str(e)
    
    return openai_api_key, None
