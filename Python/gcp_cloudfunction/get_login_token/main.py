import jwt
from flask import jsonify, make_response, request
import datetime
from quotes import quotes
from functools import wraps

SECRET_KEY = "thisis secretkey"


def get_token(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    # response = dict()
    if request.authorization and 'password' in request.authorization and 'username' in request.authorization:
        pwd = request.authorization.get('password')
        user = request.authorization.get('username')
        if pwd == 'password':
            token = jwt.encode({"user": user,
                                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=20)}, SECRET_KEY,
                               algorithm="HS256")

            return jsonify({'token': token})

        return make_response("basic login required", 404, {"www-authenticate": "basic login required"})


def authentication_required(f):
    '''
    :param f: function to wrap
    :return: new function with mandatory authentication
    '''
    @wraps(f)
    def decorated(*args, **kwrgs):
        # http://127.0.0.1:5000/xyz?token=jwt_token
        auth = request.headers.get('Authorization')
        token = auth.split()[1] if auth else None
        if not token:
            return jsonify({"msg": "required authentication token "}), 402
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.DecodeError as e:
            print(e)
            return jsonify({"msg": "unable to authenticate "}), 401
        except jwt.ExpiredSignatureError as e:
            return jsonify({"msg": "Token expired get the new one "}), 401
        else:
            return f(*args, **kwrgs)
    return decorated


@authentication_required
def get_quote_summary(request):
    orgs = 'orgs'
    if request.method == 'GET':
        return jsonify({'Listed_Orgnisations': list(quotes.keys())})
    if request.method == "POST":
        request_json = request.get_json()
        response = dict()
        if orgs in request_json:
            for org in request_json[orgs]:
                response[org] = quotes[org] if org in quotes.keys() else None
            return jsonify(response)
        return jsonify({'Error': f'Missing list of {orgs}'})

# python3 -m functions_framework --target get_token
# http://127.0.0.1:8080/get_token
