from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, DevOps!"
def greet(name):
    if not name:
        return "Hello, Guest!"
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("DevOps"))
    app.run(host="0.0.0.0", port=5000)
