from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "This is a dummy page <br> Wecome to Jenkins"


if __name__ == '__main__':
    app.run(port=8181, debug=True)