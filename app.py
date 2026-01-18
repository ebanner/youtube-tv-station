from flask import Flask, Response

from datetime import datetime


app = Flask(__name__)


START_STRING = "2026-01-18T15:21:37.690583"

START = datetime.fromisoformat(START_STRING)


def get_offset(video_length=13938):
    elapsed = datetime.now() - START
    seconds_since = elapsed.seconds
    offset = seconds_since % video_length
    return offset


@app.get("/")
def index():
    offset = get_offset()

    html = """

    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Lex Fridman TV</title>
        <style>
        body { margin: 0; display: grid; place-items: center; min-height: 100vh; }
        </style>
    </head>
    <body>
        <iframe
        width="560"
        height="315"
        src="https://www.youtube.com/embed/14OPT6CcsH4?start={{OFFSET}}&autoplay=1&mute=1"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen>
        </iframe>
    </body>
    </html>

    """.replace("{{OFFSET}}", str(offset))


    return Response(html, mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

