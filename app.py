from flask import Flask
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

@app.route('/')
def hello_world():
    return 'Hello, World from Leeza Etzenhouser in 3308!'


@app.route('/db_test')
def testing():
    conn = psycopg2.connect(DATABASE_URL)
    conn.close()
    return "Database connection successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"