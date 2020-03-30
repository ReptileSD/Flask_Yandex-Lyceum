from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def title():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lst = ['Человечество вырастает из детства.',
           'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.',
           'И начнем с Марса!',
           'Присоединяйся!']
    return '</br>'.join(lst)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='photos/mars.png')}"
                     alt="здесь должна была быть картинка, но не нашлась">
                    <p>Это подпись под картинкой Марса</p>
                  </body>
                </html>""".format()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
