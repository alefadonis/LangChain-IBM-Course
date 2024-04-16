import os
from langchain.llms import OpenAI
#from langchain.chat_models import ChatOpenAI
import gradio as gr

# assign API key
# os.environ["OPENAI_API_KEY"] = "YOUR API KEY"

gpt3 = OpenAI(model_name="text-ada-001" )

def chatbot(inpt):
    return gpt3(inpt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860)