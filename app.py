from flask import Flask, render_template, url_for, flash, redirect, request, session, g
import sqlite3
import os
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['DATABASE'] = os.path.join(app.root_path, 'database.db')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

def get_db_connection():
    conn = sqlite3.connect('database.db') 
    conn.row_factory = sqlite3.Row 
    return conn

def get_user(user_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM users WHERE user_id = ?',
                        (user_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE post_id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route("/")
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        pass_word = request.form['pass_word']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (username, pass_word) VALUES (?, ?)',
                        (username, pass_word))
        user_id = cur.lastrowid
        conn.commit()
        conn.close()
        return redirect(url_for('profile', user_id=user_id))
    else:
        return render_template('register.html')

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'pass_word' in request.form:
        username = request.form['username']
        pass_word = request.form['pass_word']
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT user_id FROM users WHERE username=? AND pass_word=?', (username, pass_word))
        user_id = c.fetchone()
        conn.close()
        if user_id:
            session['user_id'] = user_id[0]
            if 'user_id' in session:
                return redirect(url_for('profile', user_id=session['user_id']))
            else:
                return redirect(url_for('login'))
        else:
            return 'Invalid username or password.'
    else:
        return render_template('login.html')

@app.route("/timeline/<int:user_id>", methods=['GET', 'POST'])
def timeline(user_id):
    user = get_user(user_id)
    conn = get_db_connection()
    posts = conn.execute('SELECT posts.*, users.username FROM posts JOIN users ON posts.user_id = users.user_id ORDER BY posts.post_id DESC').fetchall()
    conn.close()
    return render_template('timeline.html', user=user, posts=posts)

@app.route("/profile/<int:user_id>", methods=['GET', 'POST'])
def profile(user_id):
    user = get_user(user_id)
    conn = get_db_connection()
    post_count = conn.execute('SELECT COUNT(*) FROM posts WHERE user_id = ?', (user_id,)).fetchone()[0]
    conn.close()
    return render_template('profile.html', user=user, post_count=post_count)

@app.route("/profile/<int:user_id>/posts", methods=['GET', 'POST'])
def profileposts(user_id):
    user = get_user(user_id)
    conn = get_db_connection()
    posts = conn.execute('SELECT posts.*, users.username FROM posts JOIN users ON posts.user_id = users.user_id WHERE posts.user_id = ? ORDER BY posts.post_id DESC', (user_id,)).fetchall()
    conn.close()
    return render_template('timeline.html', user=user, posts=posts)

@app.route("/profile/<int:user_id>/create", methods=['GET', 'POST'])
def create(user_id):
    user = get_user(user_id)

    if request.method == 'POST':
        pic = request.files['pic'].read() if 'pic' in request.files else None
        content = request.form['content']

        conn = get_db_connection()
        conn.execute('INSERT INTO posts (pic, content, user_id) VALUES (?, ?, ?)',
                     (pic, content, user_id))
        conn.commit()
        conn.close()
        return redirect(url_for('profile', user_id=user_id))

    return render_template('newPost.html', user=user)

@app.route('/profile/<int:user_id>/editProfile', methods=['GET', 'POST'])
def edit_profile(user_id):
    user = get_user(user_id)

    if request.method == 'POST':
        pic = request.files['pic'].read() if 'pic' in request.files else None
        bio = request.form['bio']

        conn = get_db_connection()
        conn.execute('UPDATE users SET pic = ?, bio = ?'
                         ' WHERE user_id = ?',
                         (pic, bio, user_id))
        conn.commit()
        conn.close()
        return redirect(url_for('profile', user_id=user_id))

    return render_template('editProfile.html', user=user)

@app.route('/comments/<int:user_id>/<int:post_id>', methods=['GET', 'POST'])
def comments(user_id, post_id):
    user=get_user(user_id)
    post=get_post(post_id)
    conn = get_db_connection()
    comments = conn.execute('SELECT * FROM comments WHERE post_id = ? ORDER BY comment_id DESC', (post_id,)).fetchall()
    conn.close()
    return render_template('displayComments.html', user=user, post=post, comments=comments)

@app.route('/comments/<int:user_id>/<int:post_id>/new', methods=['GET', 'POST'])
def newComment(user_id, post_id):
    user=get_user(user_id)
    post=get_post(post_id)
    if request.method == 'POST':
        content = request.form['content']
        conn = get_db_connection()
        conn.execute('INSERT INTO comments (content, user_id, post_id) VALUES (?, ?, ?)',
                     (content, user_id, post_id))
        conn.commit()
        conn.close()
        return redirect(url_for('comments', user_id=user_id, post_id=post_id))
    else:
        return render_template('addComments.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)