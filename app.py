from op import Flask, render_template # Import render_template function to render the template of template folder     

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def about():
    return "<p>About page</p>"


if __name__ == "__main__":
    app.run(debug=True, port=8000)