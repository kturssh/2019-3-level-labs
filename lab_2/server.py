from flask import Flask, render_template, redirect, url_for
import json
import secondtry

app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
def open_page(path='http://ru-good.ru/category/science'):
    secondtry.get_html_page(path)
    with open("articles.json", encoding="UTF-8") as f:
        j_strings = json.load(f)
        return render_template("index.html", articles=j_strings['articles'], url=['url'])


@app.route('/action')
def refresh():
    return redirect(url_for('open_page'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
