from setuptools import setup, find_packages

setup(
    name='cloud-engineer-ai',
    version='0.1',
    description="Cloud-engineer-ai is a Python package that generates cloud architecture diagrams based on user prompts using OpenAI's GPT models.",
    author='Deepak Chawla',
    author_email='deepakchawla35@gmail.com',
    url='https://github.com/deepakchawla/cloud-engineer-ai',
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[  # List your package dependencies here
        'diagrams',
        'openai',
        'spacy',
    ],
)
