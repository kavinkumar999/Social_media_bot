from flask import Flask
from instabot import Bot

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    print("asdf")
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug = True)

