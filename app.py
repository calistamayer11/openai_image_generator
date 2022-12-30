from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import openai


load_dotenv()

openai_key = os.getenv("OPENAI_KEY")
openai.api_key = openai_key

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.post("/generate")
def generate():
    data = request.get_json()
    prompt = data.get("prompt")
    # size = data.get("size")
    print(data)
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    image_url = response["data"][0]["url"]
    # image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-OyWg1m4thI5uxfrTmVFkyBG1/user-UJCsQExvhkFhb7VQHVusB70m/img-gyyssqKCCwvkTUg9atNYjNXH.png?st=2022-12-30T21%3A06%3A21Z&se=2022-12-30T23%3A06%3A21Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-12-30T15%3A47%3A35Z&ske=2022-12-31T15%3A47%3A35Z&sks=b&skv=2021-08-06&sig=isNhcMFqrxhWkuYmw6KV3eDdKc9pK2v1e4ca0Pb/utQ%3D"
    return {"url": image_url}
    # return data
