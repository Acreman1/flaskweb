from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Acreman"
    movies = [
        {"title":"战狼2","year":"2019"},
        {"title":"速度与激情8","year":"2018"},
        {"title":"叶问4","year":"2020"},
        {"title":"南方车站","year":"2019"},
        {"title":"复仇者联盟4","year":"2019"},
    ]
    return render_template("index.html",name=name,movies=movies)