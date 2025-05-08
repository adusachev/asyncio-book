from flask import Flask, jsonify
import psycopg2
import time

app = Flask(__name__)
conn_info = "dbname=mydb user=aleksei password=pass host=127.0.0.1"
db = psycopg2.connect(conn_info)

@app.route('/brands')
def brands():
    cur = db.cursor()
    cur.execute('SELECT brand_id, brand_name FROM brand')
    rows = cur.fetchall()
    cur.close()
    return jsonify([{'brand_id': row[0], 'brand_name': row[1]} for row in rows])
    # time.sleep(3)
    # print("GET brands")
    # return jsonify({"a": "b"})
    


## Run with 8 workers:
# cd ./chapter_9_web_apps/flask
# gunicorn -w 8 main:app

