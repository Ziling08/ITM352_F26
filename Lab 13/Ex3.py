import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://meme-api.com/gimme/wholesomememes'

    # Get a meme from the API
    response = requests.request('GET', url)
    meme = response.json()

    # Get the meme image and subreddit
    image = meme['url']
    subreddit = meme['subreddit']

    return render_template('meme.html',
                           image=image,
                           subreddit=subreddit)

if __name__ == '__main__':
    app.run(debug=True)
