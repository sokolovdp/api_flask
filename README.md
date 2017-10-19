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
headers: { 'Content-Type': 'application/json'}
body: { "username": "ivan", "password": "pupkin" }
```
###/auth
###/items
###/items/from/to
###/items/item_name

