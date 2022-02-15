from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/image_sample')
def image():
    return f'''<h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='Mars.png')}">
    <h3 style='color:green'>Тех, кого Земля достала</h3>
    <h3 style='color:black'>Тех, кто рвётся напролом</h3>
    <h3 style='color:red'>Ждём у Алого Причала!</h3>
    <h3 style='color:gray'>Mars_for_people.com</h3>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

