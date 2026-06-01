from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Cursor Learn App",
        message="Hi Nikita — a minimal Python web app for learning Cursor and deployment.",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
