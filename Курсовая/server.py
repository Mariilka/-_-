from flask import Flask, render_template

app = Flask(__name__)
nav = [
    { "title": "Главная", "URL": "/" },
    { "title": "Тренажеры", "URL": "/tren" },

    { "title": "Сделай первый шаг", "URL": "/review" },
    { "title": "Обо мне", "URL": "/aboutme" },
    { "title": "Глоссарий", "URL": "/gloss" },
]
@app.context_processor
def global_context():
    return{
        "nav": nav
    }

@app.route("/")
def index():

    return render_template("index.html", name = "Главная")

@app.route("/tren")
def tren():
    return render_template("tren.html", name = "Тренажеры")


@app.route("/pool")
def pool():
    return render_template("pool.html", name="Бассейн")

@app.route("/review")
def riview ():
    return render_template("review.html", name="Сделай первый шаг")

@app.route("/aboutme")
def aboutme():

    return render_template("aboutme.html", name = "Обо мне")

@app.route("/gloss")
def gloss():

    return render_template("gloss.html", name = "Глоссарий")