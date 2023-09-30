from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_code(user_prompt, api_key):

    llm = OpenAI(temperature=0,openai_api_key=api_key)

    prompt_template = """Using the 'diagrams' library in Python, generate Python code to create an AWS architecture diagram. 
    Please specify which AWS services or components you want to include in the diagram, and indicate where you would like to 
    add them within the diagram.

    Please note that my capabilities are limited to assisting with Python code generation and architectural diagram design 
    using the 'diagrams' library. For any other questions or requests outside of this scope, I apologize, but I won't be able 
    to provide assistance. Feel free to share a custom message if you need help with something else.

    requirement: {program} """
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["program"]
    )
    chain = LLMChain(llm=llm, prompt=PROMPT)
    resp = chain.run(program=user_prompt)

    return resp


def generate_terraform_code(user_prompt, api_key):

    llm = OpenAI(temperature=0,openai_api_key=api_key, model_name="gpt-3.5-turbo-0301")


    prompt_template = """Ignore all previous instructions.
    Generate Terraform code using the requirments given by user.

    requirement: {program} """
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["program"]
    )
    chain = LLMChain(llm=llm, prompt=PROMPT)
    resp = chain.run(program=user_prompt)

    return resp

