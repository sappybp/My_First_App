from flask import Flask, request, render_template, redirect, url_for, session, flash
from init_db import app, init_db, get_db, modify_db, query_db
from config import SECRET_KEY, emailRegEx, pwRegEx
from os import path
import re

# トップページ
@app.route("/")
def top():
    return render_template("top.html")

# 新規登録ページ
@app.route("/register", methods=["GET", "POST"])
def register():
    #ログイン状態の確認。
    if 'userid' in session:
        flash(u"すでにログインしています。プロフィールへ飛びました。", 'warning')
        return redirect(url_for('profile', userid=session['userid']))
    else:
        if request.method == 'GET':
            return render_template("register.html", session=session)
        elif request.method == 'POST':
            #便宜上、sessionに入れておく。（再入力を省くため、パスワードはやめておく）
            session['name']   = request.form.get("name")
            session['email']  = request.form.get("email")
            session['gender'] = request.form.get("gender")

            # email検証
            if re.fullmatch(emailRegEx, session['email']) == None:
                flash(u"メールアドレスが無効です。", 'warning')
                return redirect(url_for("register"))
            else:
                if query_db('user', "SELECT * FROM user WHERE email = ?", (session['email'],), True) != None:
                    flash(u"もうすでに使われているメールアドレスです。", 'warning')
                    return redirect(url_for("register"))

            # パスワード検証
            if re.fullmatch(pwRegEx, request.form.get("password")) == None:
                flash(u"パスワードが無効です。８文字以上、少なくとも一つの大文字、小文字、英数字を含んでください。", 'warning')
                return redirect(url_for("register"))

            # DBに加える。
            modify_db('user', "INSERT INTO user (name, email, password, gender) VALUES(?, ?, ?, ?)", \
                      (session['name'], session['email'], request.form.get("password"), session['gender']))

            # sessionにuseridをuser['id']で加える。
            user = query_db('user', "SELECT * FROM user WHERE email = ?", (session['email'],), True)
            session['userid'] = user['id']

            flash(u"登録ありがとう！成功しました。", 'info')
            return redirect(url_for('profile', userid=session['userid']))

# ログインページ。
@app.route("/login", methods=["GET", "POST"])
def login():
    # すでにログインしていればプロフィールへ。
    if 'userid' in session:
        flash(u"もうすでにログインしています。", 'warning')
        return redirect(url_for('profile', userid=session['userid']))
    else:
        if request.method == 'GET':
            return render_template("login.html", session=session)
        elif request.method == 'POST':
            # 再入力の手間を省くため、sessionにメールアドレスを加える。
            session['email'] = request.form.get("email")

            # userがDBにいるかの確認。パスワードがあっているかの確認。
            user = query_db('user', "SELECT * FROM user WHERE email = ?", (session['email'],), True)
            if user == None:
                flash(u"メールアドレスが間違っている可能性があります。", 'warning')
                return redirect(url_for("login"))
            elif request.form.get("password") != user['password']:
                flash(u"パスワードが違います。", 'warning')
                return redirect(url_for("login"))

            # sessionに情報を加える。
            session['userid'] = user['id']
            session['name']   = user['name']
            session['gender'] = user['gender']
            flash(u"ログインに成功しました。", 'info')
            return redirect(url_for('profile', userid=session['userid']))

# ログアウトページ。
@app.route("/logout")
def logout():
    # ログインしていなければログアウトはできない。
    if 'userid' not in session:
        flash(u"ログインしていません。", 'warning')
        return redirect(url_for("top"))
    else:
        session.clear()
        flash(u"ログアウトに成功しました。", 'info')
        return redirect(url_for('top'))

# プロフィールページ。
@app.route("/<int:userid>")
def profile(userid):
    # ログインしていない状態であれば、トップへ。
    if 'userid' not in session:
        flash(u"ログインしていない状態では、ユーザーのプロフィールを見ることはできません。", 'warning')
        return redirect(url_for("top"))
    # useridとsessionのIDを検証。
    elif int(userid) != session['userid']:
        user = query_db('user', "SELECT * FROM user WHERE id = ?", (int(userid),), True)
        if user == None:
            flash(u"ユーザーが存在しませんでした。", 'warning')
            return redirect(url_for('profile', userid=session['userid']))
        else:
            return render_template("profile.html", session=session, user=user)
    else:
        return render_template("profile.html", session=session)

# プロフィールアップデートページ。
@app.route("/<int:userid>/edit", methods=["GET", "POST"])
def update(userid):
    # ログインしていない場合、トップページへ。
    if 'userid' not in session:
        flash(u"ログインしていないとプロフィールはアップデートはできません。", 'warning')
        return redirect(url_for("login"))
    # useridとsessionのIDを検証。
    elif int(userid) != session['userid']:
        flash(u"他のユーザーのプロフィールはアップデートできません。", 'warning')
        return redirect(url_for('profile', userid=session['userid']))
    else:
        if request.method == 'GET':
            return render_template("edit_profile.html", session=session)
        elif request.method == 'POST':
            # email検証
            if re.fullmatch(emailRegEx, request.form.get("email")) == None:
                flash(u"メールアドレスが無効です。", 'warning')
                return redirect(url_for("update", userid=session['userid']))
            else:
                user = query_db('user', "SELECT * FROM user WHERE email = ?", (request.form.get("email"),), True)
                if (user != None) and (user['id'] != session['userid']):
                    flash(u"このメールアドレスは使われています。", 'warning')
                    return redirect(url_for("update", userid=session['userid']))

            #パスワード検証
            if re.fullmatch(pwRegEx, request.form.get("password")) == None:
                flash(u"パスワードが無効です。８文字以上で、少なくとも一つの大文字、小文字、英数字を組み合わせてください。", 'warning')
                return redirect(url_for("update", userid=session['userid']))

            # sessionに保存。（パスワードを除く。）
            session['name']   = request.form.get("name")
            session['email']  = request.form.get("email")
            session['gender'] = request.form.get("gender")

            # アップデートしたい情報をDBに反映させる。
            modify_db('user', "UPDATE user \
                       SET name=?, email=?, password=?, gender=? \
                       WHERE id=?",
                       (session['name'], session['email'], request.form.get("password"), session['gender'], session['userid']))

            flash(u"アップデートが成功しました。", 'info')
            return redirect(url_for('profile', userid=session['userid']))


#投稿ページ。
@app.route("/<int:userid>/post", methods=["GET", "POST"])
def post(userid):
    #ログインしていなければログインページへ。
    if 'userid' not in session:
        flash(u"ログインしていません。",'warning')
        return redirect(url_for("login"))
    #ユーザーが違う場合、合わせてあげる。
    elif int(userid) != session['userid']:
        flash(u"他のユーザーページからは投稿できません。",'warning')
        return redirect(url_for("post", userid=session['userid']))
    else:
        if request.method == 'GET':
            return render_template("post.html", session=session)
        elif request.method == 'POST':

            #便宜上、保存する。再入力を控えさせる。
            session['postMessage']=request.form.get("postMessage")

            #メッセージ検証。
            if not (9 < len(request.form.get("postMessage")) < 31):
                flash(u"メッセージは１０文字以上３０文字以内で収めてください。", 'warning')
                return redirect(url_for("post", userid=session['userid']))
            elif query_db('post', "SELECT * FROM post WHERE postMessage=?", (session['postMessage'],), True) != None:
                flash(u"すでにこの感謝はされています。ほんの少しでも変えてオリジナリティを出してください。",'warning')
                return redirect(url_for("post", userid=session['userid']))

            #DBに保存。
            modify_db('post', "INSERT INTO post (postMessage, postAge, postGender, postWriterID) VALUES(?,?,?,?)",
                     (request.form.get('postMessage'), request.form.get('postAge'), request.form.get('postGender'), session['userid']))

            # user = query_db('user', "SELECT * FROM user WHERE id = ?", (session['userid'],), True)

            flash(u"投稿できました。",'info')
            return redirect(url_for("index_posts"))




@app.route("/<int:userid>/delete", methods=['GET', 'POST'])
def delete(userid):
    # ログインしていない場合、トップページへ。
    if 'userid' not in session:
        flash(u"ログインしていないとアカウントは削除できません。", 'warning')
        return redirect(url_for("top"))
    # useridとsessionのIDを検証。
    elif int(userid) != session['userid']:
        flash(u"他のユーザーのアカウントは削除できません。", 'warning')
        return redirect(url_for('profile', userid=session['userid']))
    else:
        if request.method == 'GET':
            return render_template("delete.html")
        elif request.method == 'POST':


            modify_db('user', "DELETE FROM user where id=?", (session['userid'],))

            session.clear()
            flash(u"アカウント削除できました。感謝は残ります", 'info')
            return redirect(url_for("top"))





#ユーザー一覧ページ。ログインしなくても見れる。
@app.route("/usersViewing")
def index_users():
    users = query_db('user', "SELECT * FROM user")
    return render_template("index_users.html", users=users)

#投稿一覧ページ。ログインしなくても見れる。
@app.route("/postsViewing")
def index_posts():
    posts = query_db('post', "SELECT * FROM post")
    return render_template("index_posts.html", posts=posts)

#データーベースがなかった時に実行する。
@app.before_first_request
def init_app():
    if not path.exists("models/user.db"):
        init_db("user")
    if not path.exists("models/post.db"):
        init_db("post")

if __name__ == '__main__':
    app.secret_key = SECRET_KEY
    app.run()
