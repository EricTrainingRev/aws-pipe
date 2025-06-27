from  flask import Flask

app = Flask(__name__)

@app.get("/greeting/<name>")
def greeting(name: str):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
