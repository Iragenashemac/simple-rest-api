from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

#in memory user store
users ={}

@app.route('/users', methods=['POST'])

def create_users():
    data = request.get_json()
    print("DEBUG: Received data =",data)

    if not data:
          return jsonify({"error":"Invalid JSON"}),400
    
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
         return jsonify({"error": "Missing 'name' or  'email'"}), 400
    
    user_id = str(uuid.uuid4())
    user = {
         "id": user_id,
         "name": name,
         "email": email
    }

    users[user_id] = user
    return jsonify(user),201

@app.route('/users/<user_id>', methods =['GET'])
def get_user(user_id):
     user = users.get(user_id)

     if not user:
          return jsonify({"error": "User not found"}), 404
     
     return jsonify(user), 200

if __name__=='_main_':
     app.run(debug=True)