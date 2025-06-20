# Simple REST API

## Language and frame work
-python3 & Flask framework

## How to run


```bash
step1: clone the repo
git clone https://github.com/iragenashemac/simple-rest-api.git
cd simple-rest-api

step2:# install the Flask dependencies
pip install -r requiements.txt # this contains the name Flask and will replace the requirements.txt

step3:# run the app.py
python app.py

# The api will be avialable at, http://localhost:5000

 Example Requests

   #Create a User:

curl -X POST http://localhost:5000/users \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john@example.com"}'

  #Get a User by ID:

curl http://localhost:5000/users/<user_id> #replace the <user_id> with the actual id hashed generated id
