import requests
from flask import Flask, render_template, url_for
from flask import request 
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize", methods=['GET', 'POST'])
def Summarize():
    if request.method == 'POST':
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        TOKEN = " Your Hugging Face API token"  
        headers = {"Authorization": f"Bearer {TOKEN}"}
        min_length = 20
        max_length = int(request.form["maxL"])
        input_text = request.form["data"]

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": input_text,
            "parameters": {"min_length": min_length, "max_length": max_length}
        })[0]

        return render_template("index.html", result=output["summary_text"])
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
