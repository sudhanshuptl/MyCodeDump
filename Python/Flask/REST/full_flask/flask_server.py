from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)

app.config['secret_key'] = 'ThisISSECRET'
app.config['SQLALCHEMY_DATABASE_URI']=\
    'sqlite://///Users/iopexses/Documents/Github/Interview-Preparation/Schlumberger/rest_demo/todo.db'

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


@app.route('/user', methods=['GET'])
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



if __name__ == '__main__':
    app.run(debug=True)
