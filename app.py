from flask import Flask
from instabot import Bot

app = Flask(__name__)
app.debug = True

@app.route('/')
def initialbot():
    bot = Bot()
    # bot.login()
    # bot.upload_photo(caption="hello",photo="work.jpg")
    bot.unfollow(user_id="leomessi")
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug = True)
    # socketio.run(app)

