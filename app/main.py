from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Security Pipeline"

if __name__ == "__main__":
    app.run()