from watchlist import app,db
from flask import Flask,url_for,render_template,flash,redirect,request
from flask_login import login_user,logout_user,login_required,current_user
from watchlist.models import User,Movie

# views 视图函数
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
        title = request.form.get('title')
        year = request.form.get('year')
        if not title or not year or len(year)>4 or len(title)>60:
            flash("输入错误")
            return redirect(url_for('index'))
        movie = Movie(title=title,year=year)
        db.session.add(movie)
        db.session.commit()
        flash('插入成功')
        return redirect(url_for('index'))

    movies = Movie.query.all()
    return render_template("index.html",movies=movies)

@app.route('/movie/edit/<int:movie_id>',methods=['GET','POST'])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == "POST":
        title = request.form.get("title")
        year = request.form.get("year")
        if not title or not year or len(year)>4 or len(title)>60:
            flash('输入有误')
            return redirdect(url_for('edit'),movie_id=movie_id)
        movie.title = title
        movie.year = year
        db.session.commit()
        flash("电影更新完成")
        return redirect(url_for("index"))
    context = {"movie":movie}
    return render_template("edit.html",**context)


@app.route('/movie/delete/<int:movie_id>',methods=['GET','POST'])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash("删除完成")
    return redirect(url_for('index'))


@app.route('/login',methods=['GET','POST'])
# @login_required
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            flash('输入有误')
            return redirect(url_for('login'))
        user = User.query.first()
        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('登陆成功')
            return redirect(url_for('index'))
        flash('验证失败')
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('退出成功')
    return redirect(url_for("index"))

@app.route('/setting',methods=["GET","POST"])
@login_required
def setting():
    if request.method == 'POST':
        name = request.form.get("title")
        if not name or len(name)>20:
            flash("输入错误")
            return redirect(url_for("setting"))
        current_user.name = name
        db.session.commit()
        flash('名字已更新')
        return redirect(url_for('index'))
    return render_template('setting.html')


