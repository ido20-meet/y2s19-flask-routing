from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html") 

@app.route('/hello/<string:name>')
def hello_name_route(name):
	return render_template('home.html', n=name)

@app.route('/name/<int:student_id>')
def display_student(student_id=1):
	return render_template('student.html', id_number=student_id, Student=query_by_id(student_id))


if __name__ == '__main__':
	app.run(debug=True)
