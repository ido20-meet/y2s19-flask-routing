from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html") 

@app.route('/hello')
def hello_route():
	return render_template('Hello.html', n='Emily')



if __name__ == '__main__':
    app.run(debug=True)
