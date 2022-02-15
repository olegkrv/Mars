'''from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('base.html', title='Домашняя страница',
                           username=user)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def do():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

