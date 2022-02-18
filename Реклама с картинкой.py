from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/image_sample')
def image():
    return f'''<h1>Жди нас, Марс!</h1>
 <img src="{url_for('static', filename='Mars.png')}">
 <h3 style='color:green'><p style="background-color: #CFFFBA">Тех, кого Земля достала</p></h3>
 <h3 style='color:black'><p style="background-color: #BDBDBD">Тех, кто рвётся напролом</p></h3>
 <h3 style='color:red'><p style="background-color: #FFBABA">Ждём у Алого Причала!</p></h3>
 <h3 style='color:gray'><p style="background-color: #EFEFEF">Mars_for_people.com</p></h3>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
