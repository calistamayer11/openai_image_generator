from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import openai


load_dotenv()

openai_key = os.getenv("OPENAI_KEY")
openai.api_key = openai_key

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.post("/generate")
def generate():
    data = request.get_json()
    prompt = data.get("prompt")
    size = data.get("size")
    try:
        response = openai.Image.create(prompt=prompt, n=1, size=size)
        image_url = response["data"][0]["url"]
    except openai.error.OpenAIError as e:
        return {"error": e}
    except Exception as e2:
        return {"error": e2}

    return {"url": image_url}
