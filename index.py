# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import time

application = Flask(__name__)

@application.route('/')
def hello_world():
    while(True):
		milliseconds = int(round(time.time() * 1000))
		if (int(round(time.time() * 1000)) > milliseconds + 1000):
			print("ciao")
			milliseconds = int(round(time.time() * 1000))
		