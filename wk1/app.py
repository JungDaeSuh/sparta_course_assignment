from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta_plus_week1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/journal', methods=['GET'])
def show_journal():
    journals = list(db.journal.find({}, {'_id': False}))
    return jsonify({'all_journals': journals})

@app.route('/journal', methods=['POST'])
def save_journal():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    doc = {
        'title': title_receive,
        'content': content_receive
    }

    db.journal.insert_one(doc)

    return jsonify({'msg': '저장장 완료'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

