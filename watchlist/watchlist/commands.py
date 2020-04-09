import click
from watchlist import db,app
from watchlist.models import User,Movie

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



# 生成管理员账号flask admin
# 输入用户名admin，密码，确认密码
@app.cli.command()
@click.option('--username',prompt=True,help='登陆用户')
@click.option('--password',prompt=True,help='登陆密码',confirmation_prompt=True,hide_input=True)
def admin(username,password):
    user = User.query.first()
    if user is not None:
        click.echo('更新管理员账户')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建管理员账户')
        user = User(username=username,name='Admin')
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo('管理员账号操作成功')