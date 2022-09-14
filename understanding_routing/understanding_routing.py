from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/dojo')
def say_dojo():
    return "Dojo!"


@app.route('/say/<name>')
def hello_name(name):
    return "Hello " + name


@app.route('/repeat/<int:rep>/<word>')
def repeat_word(rep, word):
    str = ""
    for i in range(0, rep, 1):
        str += word+"</br>"
    return str


@app.errorhandler(404)
def handle_404(e):
    return "Not Found, but I can always handle it"


if __name__ == "__main__":
    app.run(debug=True)
