from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f'Hello, World! DB Version: {db_version}'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
