from flask import Flask, jsonify, request, make_response
import  jwt
import datetime
from functools import wraps


app = Flask(__name__)
app.config['SECRET'] = 'thisis secretkey'


def authentication_required(f):
    '''
    :param f: function to wrap
    :return: new function with mandatory authentication
    '''
    @wraps(f)
    def decorated(*args, **kwrgs):
        # http://127.0.0.1:5000/xyz?token=jwt_token
        token = request.args.get('token')
        if not token:
            return jsonify({"msg": "required authentication token "}), 402
        try:
            jwt.decode(token, app.config['SECRET'])
        except jwt.DecodeError as e:
            return jsonify({"msg": "unable to authenticate "}), 401
        except jwt.ExpiredSignature as e:
            return jsonify({"msg": "Token expired get the new one "}), 401
        else:
            return f(*args, **kwrgs)
    return decorated


@app.route("/public")
def open_func():
    return jsonify({"msg": "anyOne can access this"})


@app.route('/private')
@authentication_required
def private_data():
    # http://127.0.0.1:5000/private?token=jwt_token
    return jsonify({'msg': 'This is very private data'})


@app.route("/login", methods=['POST'])
def login():
    auth = request.authorization
    if auth and auth.password == "password":
        # token get expired after given time for now its 2 minute
        token = jwt.encode({"user": auth.username,
                           'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=2)},app.config['SECRET'])
        return jsonify({'token': token.decode("UTF-8")})

    return make_response("Not able to verify",404,{"www-authenticate": "basic login required"})


if __name__ == '__main__':
    app.run(debug=True)