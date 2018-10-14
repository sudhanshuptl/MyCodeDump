from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_details():
    headline = 'Hello World'
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        print(request.form.get("case_id"))
        return 'got post request'


if __name__ == '__main__':
    app.run(debug=True)