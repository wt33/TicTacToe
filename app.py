from flask import Flask
from tictactoe import main

app = Flask(__name__)


@app.route('/')
def hello_world():
    return main()


if __name__ == '__main__':
    app.run(debug=True)
