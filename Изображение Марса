from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/image_mars')
def image():
    return f'''<h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='D:/prohramming/git_ptoject/Mars.png')}">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
