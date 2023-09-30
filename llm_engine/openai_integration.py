from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_code(user_prompt, api_key):

    llm = OpenAI(temperature=0,openai_api_key=api_key)

    prompt_template = """Ignore all previous instructions.
    Generate Python code using the 'diagrams' library to create an AWS architecture diagram.

    requirement: {program} """
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["program"]
    )
    chain = LLMChain(llm=llm, prompt=PROMPT)
    resp = chain.run(program=user_prompt)

    return resp

