from flask import render_template, Flask, request, json, send_from_directory
import os
app = Flask(__name__, static_folder='./static')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/map')
def map():
    return render_template("map.html")

@app.route('/detail1')
def detail1():
    return render_template("detail1.html")


if __name__ == "__main__":
	app.run()