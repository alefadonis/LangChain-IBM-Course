from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
import wget
import os
import gradio as gr

# link to a text document
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0W2REN/images/state_of_the_union.txt"
output_path = "state_of_the_union.txt"  # Local the file

# Check if the file already exists
if not os.path.exists(output_path):
    # Download the image using wget
    wget.download(url, out=output_path)

loader = TextLoader('state_of_the_union.txt')

# Load the data loader
data = loader.load()

# Create the index instance that makes it searchable
index = VectorstoreIndexCreator(embedding=OpenAIEmbeddings()).from_loaders([loader])

# Running into Gradio
def summarize(ind, query):

    return index.query(query)

iface = gr.Interface(fn=summarize, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0", server_port= 7860)