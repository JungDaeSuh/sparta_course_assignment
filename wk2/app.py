from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    my_name = "Sparta"
    return render_template('index.html', name=my_name)

@app.route('/detailed/<keyword>')
def detail(keyword):  # put application's code here
    r = requests.get(f"https://owlbot.info/api/v4/dictionary/{keyword}", headers={"Authorization": "Token 605d8ee2c21155342169d23e1e421a42eb26e9d1"})
    result = r.json()
    print(result)
    word_receive = request.args.get("word_give")
    print(word_receive)
    return render_template('detailed.html', word=keyword)


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
#     return render_template("detailed.html")
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)