from flask import Flask, request, jsonify, make_response
from flask_mysqldb import MySQL
import os
import uuid
from werkzeug.security import generate_password_hash, check_password_hash 
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
dbpass = os.getenv('dbpassword')
app.config['SECRET_KEY'] = "ovojemojtajnikljuc"
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = dbpass
app.config['MYSQL_DB'] = 'rest_api'


db = MySQL(app)
app.app_context().push()
# class User():
#     cur = db.connect.cursor()
#     query = "CREATE TABLE rest_api (id INT NOT NULL PRIMARY KEY,public_id INT, name  VARCHAR(40),password VARCHAR(30), is_admin BOOLEAN)"
#     cur.execute(query)
#     db.connect.commit()
#     cur.close()

# class Todo():
#         cur = db.connect.cursor()
#         query = "CREATE TABLE todo (id INT NOT NULL PRIMARY KEY,public_id INT, text  VARCHAR(40),complete BOOLEAN, user_id BOOLEAN)"
#         cur.execute(query)
#         db.connect.commit()
#         cur.close()
class Insert(): # Upisivanje u bazu pomocu konstruktora promenljivih vrednosti
    def __init__(self, public_id, name, password, is_admin):    # metoda sa parametrima
        self.public_id = public_id  # deklaracija varijabli
        self.name = name
        self.password = password
        self.is_admin = is_admin

        cur = db.connection.cursor()
        query = "INSERT INTO rest_api.rest_api (public_id, name, password, is_admin) VALUES ('{0}','{1}','{2}',{3});".format(self.public_id, self.name, self.password, self.is_admin)
        cur.execute(query)
        db.connection.commit()
        cur.close()
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({"message" : "token is missing!"}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
            
            cur = db.connection.cursor()
            query = "SELECT public_id FROM rest_api.rest_api WHERE public_id = '{0}';".format(data['public_id'])
            cur.execute(query)
            var3 = cur.fetchall()
            db.connection.commit()
            cur.close()
            for key in var3:
                key
                print(key[0])
        except:
            return jsonify({"message" : "token is invalid!"}), 401
        return f(key, *args, **kwargs)
    return decorated

@app.route('/user', methods = ['GET'])
@token_required
def get_all_users(key):
    for user in key:
        
        cur = db.connection.cursor()
        query = "SELECT is_admin FROM rest_api.rest_api WHERE public_id = '{0}';".format(user)
        cur.execute(query)
        var4 = cur.fetchall()
        db.connection.commit()
        cur.close()
        for item in var4:
            

            if item[0] == 0:
                return jsonify({"message" : "Cannot preforam that fuction!"})
    output = []
    cur = db.connection.cursor()
    query = "SELECT public_id, name, password, is_admin FROM rest_api.rest_api;"
    cur.execute(query)
    db.connection.commit()
    cur.close()
    for i in cur:
        user_data = {}
        user_data['public_id'] = i[0]
        user_data['name'] = i[1]
        user_data['password'] = i[2]
        user_data['is_admin'] = i[3]
        output.append(user_data)

    
    return jsonify({"Users": output})

@app.route('/user/<public_id>', methods = ['GET'])
@token_required
def get_one_user(key, public_id):
    for user in key:
        
        cur = db.connection.cursor()
        query = "SELECT is_admin FROM rest_api.rest_api WHERE public_id = '{0}';".format(user)
        cur.execute(query)
        var4 = cur.fetchall()
        db.connection.commit()
        cur.close()
        for item in var4:
            

            if item[0] == 0:
                return jsonify({"message" : "Cannot preforam that fuction!"})   
 
    cur = db.connection.cursor()
    query = "SELECT public_id, name, password, is_admin FROM rest_api.rest_api WHERE public_id='{0}';".format(public_id)
    cur.execute(query)
    db.connection.commit()
    cur.close()

    for i in cur:
        user_data = {}
        user_data['public_id'] = i[0]
        user_data['name'] = i[1]
        user_data['password'] = i[2]
        user_data['is_admin'] = i[3]
        

    try:
        return jsonify({"Users": user_data})
    except:
        return jsonify({"Message" : "User not found"})

    
@app.route('/user', methods = ['POST'])
@token_required
def create_user(key):
    for user in key:
        
        cur = db.connection.cursor()
        query = "SELECT is_admin FROM rest_api.rest_api WHERE public_id = '{0}';".format(user)
        cur.execute(query)
        var4 = cur.fetchall()
        db.connection.commit()
        cur.close()
        for item in var4:
            
            if item[0] == 0:
                return jsonify({"message" : "Cannot preforam that fuction!"})

    data = request.get_json()

    hash_password = generate_password_hash(data['password'], method = 'sha256')
    
    Insert(str(uuid.uuid4()), data['name'], hash_password, 0) #nula simbolizuje false a jedan true
    return jsonify({"Message" : "New user created!"})


@app.route('/user/<public_id>', methods = ['PUT'])
@token_required
def promote_user(key, public_id):
    for user in key:
        
        cur = db.connection.cursor()
        query = "SELECT is_admin FROM rest_api.rest_api WHERE public_id = '{0}';".format(user)
        cur.execute(query)
        var4 = cur.fetchall()
        db.connection.commit()
        cur.close()
        for item in var4:
            

            if item[0] == 0:
                return jsonify({"message" : "Cannot preforam that fuction!"})

    cur = db.connection.cursor()
    query = "SELECT public_id, name, password, is_admin FROM rest_api.rest_api WHERE public_id='{0}';".format(public_id)
    cur.execute(query)
    query = "UPDATE rest_api.rest_api SET is_admin = '1' WHERE public_id = '{0}';".format(public_id)
    cur.execute(query)

    db.connection.commit()
    cur.close()
    try:
        return jsonify({"Message": "The user has been promoted!"})
    except:
        return jsonify({"Message" : "User not found"})



    return ""

@app.route('/user/<public_id>', methods = ['DELETE'])
@token_required
def delete_user(key, public_id):
    for user in key:
        
        cur = db.connection.cursor()
        query = "SELECT is_admin FROM rest_api.rest_api WHERE public_id = '{0}';".format(user)
        cur.execute(query)
        var4 = cur.fetchall()
        db.connection.commit()
        cur.close()
        for item in var4:
            

            if item[0] == 0:
                return jsonify({"message" : "Cannot preforam that fuction!"})

    cur = db.connection.cursor()
    query = "DELETE FROM rest_api.rest_api WHERE public_id = '{0}';".format(public_id)
    cur.execute(query)
    db.connection.commit()
    cur.close()

 
    try:
        return jsonify({"Message": "The user has been deleted!"})
    except:
        return jsonify({"Message" : "User not found"})
    
@app.route('/login')
def login():
    auth = request.authorization

    cur = db.connection.cursor()
    query = "SELECT name FROM rest_api.rest_api WHERE name = '{0}';".format(auth.username)
    cur.execute(query)
    var = cur.fetchall()
    db.connection.commit()
    cur.close()

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify 0', 401, {'WWW-Authenticate' : 'Basic realm = "Login required!"'})

    for i in var:
        i = "".join(i)
        a = any(item in auth.username for item in i)
        if auth.username == i:
           
            cur = db.connection.cursor()
            query = "SELECT password FROM rest_api.rest_api WHERE name = '{0}';".format(auth.username)
            cur.execute(query)
            var1 = cur.fetchall()
            db.connection.commit()
            cur.close()
            for j in var1:
                j = "".join(j)
                if check_password_hash(j, auth.password):
                    cur = db.connection.cursor()
                    query = "SELECT public_id FROM rest_api.rest_api WHERE password = '{0}';".format(j)
                    cur.execute(query)
                    var2 = cur.fetchall()
                    db.connection.commit()
                    cur.close()
                    for value in var2:
                        value = "".join(value)
                        
                        token = jwt.encode({"public_id" : value, "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=30) }, app.config['SECRET_KEY'],algorithm='HS256')
                                                                                                      
                        return jsonify({"token": token })
                
   
    if not var:
        
        return make_response('Could not verify 1', 401, {'WWW-Authenticate' : 'Basic realm = "Login required!"'})


    

    

    return make_response('Could not verify 2', 401, {'WWW-Authenticate' : 'Basic realm = "Login required!"'})



if __name__ == "__main__":
    app.run(debug = True)
    
    #35 minut klipa