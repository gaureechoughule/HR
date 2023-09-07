from flask import Flask
from task1 import c

app = Flask(__name__)


@app.route('/task1')                        # flask --app task1_flask run
def task1():
    return c

if __name__ == "__main__":
    app.run(debug = True, port = 8000)