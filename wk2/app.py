from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    my_name = "Sparta"
    return render_template('index.html', name=my_name)

@app.route('/detail')
def detail():  # put application's code here
    return render_template('detail.html')


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