from flask import Flask
from flask import render_template
import urllib, collections, hmac, binascii, time, random, string
from flask.ext.tweepy import Tweepy
from hashlib import sha1
from twitter import *

app = Flask(__name__)

app.config.setdefault('TWEEPY_CONSUMER_KEY', 'aRahVNAuCVdWy5PGFjMoAIWui')
app.config.setdefault('TWEEPY_CONSUMER_SECRET', 'fABUmGW1uV4pnlgTpwSx8KAxQdbVH6fz2le4dEW4e9wlnxmP2b')
app.config.setdefault('TWEEPY_ACCESS_TOKEN_KEY', '2834176217-coE5CGfxIdniddoou1HOBcG3r4KVdVG2UzJQStS')
app.config.setdefault('TWEEPY_ACCESS_TOKEN_SECRET', '3tfg6G4clDY42ie6wYekxf77xHGKCZjmWtUzIEqRTHqoW')

tweepy = Tweepy(app)

@app.route('/')
def index():
    tweets = tweepy.api.public_timeline()
    return render_template('index.html', tweets=tweets)

@app.route('/test_render')
def test_render():
    message = 'screw the render, that is at the index method...'
    return message

if __name__ == '__main__':
    app.run()
