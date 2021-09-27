from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    my_name = "Sparta"
    return render_template('index.html', name=my_name)

@app.route('/detail/<keyword>')
def detail(keyword):  # put application's code here
    r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    response = r.json()
    rows = response['RealtimeCityAir']['row']
    word_receive = request.args.get("word_give")
    print(word_receive)
    return render_template('detail.html', rows=rows, word=keyword)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# from flask import Flask, render_template
#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def main():
#     return render_template("index.html")
#
#
# @app.route('/detail')
# def detail():
#     return render_template("detail.html")
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)