from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def word():
    quote = None
    try:
        response = requests.get('https://zenquotes.io/api/random')
        app.logger.info(f'response: {response}, {response.json()}')
        quote = response.json()[0]
    except Exception as e:
        app.logger.exception(f'error fetching quote')
    return quote
    #return zenquotespy.random()

if __name__ == '__main__':
    app.run(debug=True)