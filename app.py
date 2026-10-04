from flask import Flask

app = Flask(__name__)

def greet(name):
    if not name:
        return "Hello, Guest!"
    return f"Hello, {name}!"

@app.route("/")
def home():
    return greet("DevOps")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
