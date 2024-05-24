from flask import Flask, render_template,jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    name = "Aayush"  # Replace with your name
    current_time = datetime.datetime.now().strftime("%I:%M:%S")
    current_directory = os.getcwd()
    return render_template('index.html', name=name, current_time=current_time, current_directory=current_directory)

@app.route("/content/<int:age>")
def content(age):
    if age < 18:
        result = {
            "content": "You are not allowed to access this content",
            "message": "You are under 18",
            "error": 404
        }
    else:
        result = {
            "content": "You are allowed to access this content",
            "message": "Welcome to the content"
        }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False)