import os

from flask import Flask, jsonify, render_template
from giphypop import Giphy

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = app.config['SECRET_KEY']

giphy = Giphy()


@app.route('/')
def index():
    gif = get_gif()

    if not gif:
        return 'oops'
    else:
        return render_template('index.html', media_url=gif.url, width=gif.width, height=gif.height)


@app.route('/_refresh_gif')
def refresh_gif():
    gif = get_gif()
    return jsonify(media_url=gif.url, width=gif.width, height=gif.height)


def get_gif():
    tag = 'funny-cat'

    try:
        result = giphy.random_gif(tag=tag, strict=True)
    except:
        result = giphy.random_gif(tag='oops')

    return result.fixed_width if result else None


if __name__ == '__main__':
    app.run()