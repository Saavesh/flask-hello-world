import psycopg2
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Sherry Saavedra in 3308'


@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://first_database_ih70_user:IWeBo50iP8WmooP6q5ZMkSh579h8yGp3@dpg-csjijj5svqrc73esldfg-a/first_database_ih70")
    conn.close()
    return "Database Connection Successful"