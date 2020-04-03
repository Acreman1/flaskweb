import os,sys

from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
import click

WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///"  # windows平台
else:
    prefix = "sqlite:////"  # Mac,linux平台
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# models 数据层
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(24))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64))
    year = db.Column(db.String(4))

# views 视图函数
@app.route('/')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template("index.html",user=user,movies=movies)



# 自定义命令

# 建立数据库
@app.cli.command()  # 注册为命令
@click.option('--drop',is_flag=True,help="先删除再创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库')


# 向数据库中插入数据
@ app.cli.command()
def forge():
    name = "Acreman"
    movies = [
        {"title":"战狼2","year":"2019"},
        {"title":"速度与激情8","year":"2018"},
        {"title":"叶问4","year":"2020"},
        {"title":"南方车站","year":"2019"},
        {"title":"复仇者联盟4","year":"2019"},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('导入数据完成')

# 错误处理函数
@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template('404.html',user=user)

