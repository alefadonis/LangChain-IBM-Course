import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain.llms import OpenAI

# you dont need to insert API
# openai_api_key = "YOUR API KEY"
# os.environ["OPENAI_API_KEY"] = openai_api_key

# initialize the models
llm = OpenAI(
    model_name="gpt-3.5-turbo"
)

# Define a PromptTemplate to format the prompt with user input
prompt = PromptTemplate(
    input_variables=["action"],
    template="Return a step-by-step tutorial with this template:\n In order to do {action}, you need to follow these steps:\n 1.Do this\n2.Do that\n Hope this step-by-step tutorial helped you!",
)

# Define a function to generate a tutorial using the llm and user input
def generate_cover_letter(action: str) -> str:
    formatted_prompt = prompt.format(action=action)
    response = llm(formatted_prompt)
    return response

# Define the Gradio interface inputs
inputs = [
    gr.Textbox(label="Task"),
]

# Define the Gradio interface output
output = gr.Textbox(label="Step-by-step Tutorial")

# Launch the Gradio interface
gr.Interface(fn=generate_cover_letter, inputs=inputs, outputs=output).launch(server_name="0.0.0.0", server_port= 7860)