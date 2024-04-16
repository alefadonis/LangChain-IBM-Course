import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.utilities import PythonREPL

from langchain.llms import OpenAI 

#openai_api_key = "YOUR API KEY"

#os.environ["OPENAI_API_KEY"] = openai_api_key

gpt3 = OpenAI(model_name='gpt-3.5-turbo')

# Equipting the agent with some tools

tools = load_tools([ "llm-math","requests_all","human"], llm=gpt3)

# Defining the agent
agent = initialize_agent(tools, llm=gpt3, agent="zero-shot-react-description", verbose=True)
agent.run("create simple matplotlib showing sin function and plot it")