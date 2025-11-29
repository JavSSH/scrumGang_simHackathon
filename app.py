from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

# Testing Git
# updating git

if __name__ == "__main__":
    app.run()