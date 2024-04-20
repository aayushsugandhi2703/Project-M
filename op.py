from flask import Flask, render_template
import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    name = "Aayush"  # Replace with your name
    current_time = datetime.datetime.now().strftime("%I:%M:%S")
    current_directory = os.getcwd()
    return render_template('index.html', name=name, current_time=current_time, current_directory=current_directory)

if __name__ == '__main__':
    app.run(debug=True, port=9988)
