from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1> Hello World! from app_two</h2>'


@app.route('/<string:name>')
def greet(name):
    return f'<h1> Hello {name.title()}! from app_two</h1>'


if __name__ == '__main__':
    app.run()