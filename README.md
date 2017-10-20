# My RESTfull API sample
Simple API coded in Python 3.6 using **Flask-RESTful** mini-framework. 
**JWT** method is used for  authentication.
**PBKDF2** method for password hashing.
**SQLAlchemy** with *SQLite3* for database access.
## Local Installation
```
pip install -r requirements.txt
```
## To start locally
```
python app.py
```
## REST API routes
###/signup
```
request headers: { 'Content-Type': 'application/json'}
request body: { "username": "ivan", "password": "pupkin" }
response body: {"message": "user created" }
```
###/auth
```
request headers: { 'Content-Type': 'application/json'}
request body: { "username": "ivan", "password": "pupkin" }
response body: { "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciO....AplyI3I" }
```
###/items
```
request headers: { 'Authorization': 'JWT yJ0eXAiOiJKV1QiLCJhbGciO....AplyI3I'}
response body: { "total items": 2 }
```
###/items/item_name
```
request headers: { 'Authorization': 'JWT yJ0eXAiOiJKV1QiLCJhbGciO....AplyI3I'}
response body: { "name": "item_name", "price": 4444.44, "in_store": false }
```
###/items/from/to
```
request headers: { 'Authorization': 'JWT yJ0eXAiOiJKV1QiLCJhbGciO....AplyI3I'}
response body: { 
    "from": 1,
    "to": 2,
    "items": [
        {
            "name": "phone",
            "price": 33.33,
            "in_store": true
        },
        {
            "name": "fifka",
            "price": 4444.44,
            "in_store": false
        }
    ] 
}
```