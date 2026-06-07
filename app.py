from flask import Flask, request, jsonify, send_file
import httpx

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434"


@app.route("/")
def root():
    return send_file("index.html")


@app.route("/api/tags")
def tags():
    resp = httpx.get(f"{OLLAMA_URL}/api/tags", timeout=30)
    return resp.json()


@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.json
    resp = httpx.post(f"{OLLAMA_URL}/api/generate", json=data, timeout=120)
    return resp.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
