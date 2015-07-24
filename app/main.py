from flask import Flask
from flask import render_template
from twitter import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_render')
def test_render():
    twitter_stream = TwitterStream(auth=OAuth('2834176217-coE5CGfxIdniddoou1HOBcG3r4KVdVG2UzJQStS', '3tfg6G4clDY42ie6wYekxf77xHGKCZjmWtUzIEqRTHqoW', 'fABUmGW1uV4pnlgTpwSx8KAxQdbVH6fz2le4dEW4e9wlnxmP2b', 'aRahVNAuCVdWy5PGFjMoAIWui'))
    return t.statuses.user_timeline(screen_name="@ESLCS")

if __name__ == '__main__':
    app.run()
