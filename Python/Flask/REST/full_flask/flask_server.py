from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import  SQLAlchemy
import uuid, jwt, datetime
from functools import  wraps


app = Flask(__name__)

app.config['secret_key'] = 'ThisISSECRET'
app.config['SQLALCHEMY_DATABASE_URI']=\
    'sqlite://///Users/iopexses/Documents/Github/MyCodeDump/Python/Flask/REST/full_flask/todo.db'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/iopex'

# User terminal & open python3
# from flask_server import db
# db.create_all() # to create all tables for first time
# exit() # exit python cli

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)


class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80))
    is_complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)


def basic_auth_required(f):
    @wraps(f)  # this will preserver metadata and documentation of decorated FUNCTION
    def decorated(*args, **kwrgs):
        token = request.args.get('token')
        if not token:
            return jsonify({'msg': 'authentication token is required'}), 405
        try:
            jwt.decode(token, app.config['secret_key'])
        except jwt.DecodeError as e:
            return jsonify({"msg": "unable to authenticate "}), 401
        except jwt.ExpiredSignature as e:
            return jsonify({"msg": "Token expired get the new one "}), 401
        else:
            return f(*args, **kwrgs)
    return decorated


def admin_permission_required(f):
    @wraps(f)  # this will preserver metadata and documentation of decorated FUNCTION
    def decorated(*args, **kwrgs):
        token = request.args.get('token')
        if not token:
            return jsonify({'msg': 'authentication token is required'}), 405
        try:
            public_id = jwt.decode(token, app.config['secret_key']).get('public_id')
            if not public_id:
                return jsonify({'msg': 'You need admin access for this'}), 405

            user = User.query.filter_by(public_id = public_id ).first()
            if not user:
                return jsonify({'err': 'User might be recently deleted '}), 405
            if not user.admin:
                return jsonify({'err': 'Admin access required for this action'}),405
        except jwt.DecodeError as e:
            return jsonify({"msg": "unable to authenticate "}), 401
        except jwt.ExpiredSignature as e:
            return jsonify({"msg": "Token expired get the new one "}), 401
        else:
            return f(*args, **kwrgs)

    return decorated

@app.route('/user', methods=['GET'])
@basic_auth_required
def get_all_user():
    users = User.query.all()
    try:
        result = list()
        for user in users:
            result.append(dict(name = user.name,
                            public_id = user.public_id,
                            password = user.password,
                            admin = user.admin))
    except Exception as e:
        print(e)
        return jsonify({"err" : "error in fetching user details"})
    else:
        return jsonify({'users' : result}), 200

@app.route('/user/<public_id>', methods=['PUT'])
@admin_permission_required
def promote_user(public_id):
    try:
        user = User.query.filter_by(public_id=public_id).first()
        if not user:
            return jsonify({'msg':'No user with this public_id'}), 404
        else:
            user.admin = True
            db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({"err": 'Internal Error'})
    else:
        return jsonify({'msg': f'User `{user.name}` is Promoted'})
        


@app.route('/user/<public_id>', methods=['GET'])
def get_user(public_id):
    '''
    http://127.0.0.1:5000/user/0c0bfab5-a5a5-4aa5-9791-c011c33b7516
    '''
    try:
        user = User.query.filter_by(public_id=public_id).first()
        if not user:
            return jsonify({'msg':'No user with this public_id'}), 404

        result = dict(name = user.name,
                      public_id = user.public_id,
                      password = user.password,
                      admin = user.admin)
    except Exception as e:
        print(e)
        return jsonify({'err': 'Error while processing'}), 400
    else:
        return jsonify(result), 200

@app.route('/user/<public_id>', methods=['DELETE'])
@admin_permission_required
def delete_user(public_id):
    try:
        user = User.query.filter_by(public_id=public_id).first()
        if not user:
            return jsonify({'msg':'No user with this public_id'}), 404
        
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({'err': 'Internal error'})
    else:
        return jsonify({'msg': f'user : {user.name} deleted succefully'})



# http://127.0.0.1:5000/user
@app.route('/user', methods=['POST'])
@admin_permission_required
def create_user():
    '''
    http://127.0.0.1:5000/user
    payload -> json
            {
        "name":"sudhanshu",
        "password":"1234"
        }
    :return: json response
    '''
    data = request.get_json()
    try:
        hashed_password = generate_password_hash(data['password'], method='sha256')

        # create new user
        new_user = User(public_id=str(uuid.uuid4()), # it will always create unique public id using request id + timestamp
                        name=data['name'],
                        password=hashed_password,
                        admin=False
                        )
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({'msg': 'Error in creating new user'}), 406

    return jsonify({"msg": "New User created"}), 200


@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if auth and auth.username and auth.password:
        user = User.query.filter_by(name=auth.username).first()
        if not user:
            return jsonify({'err': f'user = `{auth.username}` does not exist '}), 405
        elif check_password_hash(user.password, auth.password):
            # generate jwt token
            token = jwt.encode(dict(public_id=user.public_id,
                                    exp=datetime.datetime.utcnow()+datetime.timedelta(minutes=10)),
                               app.config['secret_key'])
            return jsonify({'token': token.decode('UTF-8')}), 200
        else:
            return jsonify({'msg': 'wrong password'}), 405
    else:
        return jsonify({'msg': 'Missing credentials'})


if __name__ == '__main__':
    app.run(debug=True)
