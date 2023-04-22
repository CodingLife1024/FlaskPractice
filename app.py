from flask import Flask, render_template, url_for, flash, redirect, request, session
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db') 
    conn.row_factory = sqlite3.Row 
    return conn

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        pass_word = request.form['pass_word']

        if not username:
            flash('Username is required!')
        elif not pass_word:
            flash('Password is required!')
        else:
            conn = get_db_connection()
            existing_user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
            if existing_user:
                error = "Username already exists"
                #return render_template('register.html', error=error)
            else:
                conn.execute('INSERT INTO users (username, pass_word) VALUES (?, ?)',
                            (username, pass_word))
            conn.commit()
            conn.close()
            return render_template('index.html', error=error)

    return render_template('register.html')

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     pass_word = request.form['pass_word']

    #     # perform validation and authentication here
    #     # for example, check if username and password match a user in a database
    #     conn = sqlite3.connect('database.db')
    #     c = conn.cursor()
    #     c.execute('SELECT * FROM user_info WHERE username = ? AND pass_word = ?', (username, pass_word))
    #     user = c.fetchone()

    #     if user:
    #         # set the user_id in the session
    #         session['user_id'] = user[0]

    #         # redirect to a success page if the user is authenticated
    #         return redirect('/exp')
    #     else:
    #         # return an error message if the user is not authenticated
    #         error = 'Invalid username or password. Please try again.'
    #         return render_template('login.html', error=error)
    
    # # if the request method is GET, return the login form
    # else:
    #     return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('SELECT user_id FROM users WHERE username=? AND pass_word=?', (username, password))
        user_id = c.fetchone()
        conn.close()
        if user_id:
            session['user_id'] = user_id[0]
            return redirect('/profile')
        else:
            return 'Invalid username or password.'
    else:
        return render_template('login.html')


@app.route("/popular", methods=['GET', 'POST'])
def popular():
    return render_template('popular.html')

@app.route("/timeline", methods=['GET', 'POST'])
def timeline():
    return render_template('timeline.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_results = request.form['searchresults']
        return f'Search results for "{search_results}"'
    return render_template('search.html')

@app.route("/profile/<int:user_id>", methods=['GET', 'POST'])
def profile(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user is None:
        return 'User not found'
    return render_template('profile.html', user=user)

@app.route("/profile/followers", methods=['GET', 'POST'])
def profilefollowers():
    return render_template("followers.html")

@app.route("/profile/following", methods=['GET', 'POST'])
def profilefollowing():
    return render_template("following.html")

@app.route("/profile/posts", methods=['GET', 'POST'])
def profileposts():
    return render_template("profileposts.html")

@app.route("/profile/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if request.form['submit_button'] == 'submit':
            # do something with submitted data
            return "Comment Submitted"
        elif request.form['submit_button'] == 'discard':
            # discard submitted data
            return "Comment Discarded"
    else:
        return render_template('newPost.html')

@app.route('/profile/editProfile/<int:user_id>', methods=['GET', 'POST'])
def edit_profile(user_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
    user = c.fetchone()
    conn.close()

    if request.method == 'POST':
        bio = request.form['bio']
        pic = request.files['pic'].read() if 'pic' in request.files else user[4]
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('UPDATE users SET bio=?, pic=? WHERE user_id=?', (bio, pic, user_id))
        conn.commit()
        conn.close()
        return redirect(url_for('profile', user_id=user_id))

    return render_template('editProfile.html', user=user)



@app.route('/comments', methods=['GET', 'POST'])
def comments():
    return render_template('displayComments.html')

@app.route('/comments/new', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'submit':
            # do something with submitted data
            return "Comment Submitted"
        elif request.form['submit_button'] == 'discard':
            # discard submitted data
            return "Comment Discarded"
    else:
        return render_template('addComments.html')




@app.route('/exp')
def inde():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

# @app.route('/create/', methods=('GET', 'POST'))
# def creat():
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']

#         if not title:
#             flash('Title is required!')
#         elif not content:
#             flash('Content is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
#                          (title, content))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('login'))

#     return render_template('create.html')




if __name__ == '__main__':
    app.run(debug=True)