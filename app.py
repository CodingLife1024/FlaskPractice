from flask import Flask, render_template, url_for, flash, redirect, request
import sqlite3
from flask import session

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def add_user_to_database(username, password):
    # Open a connection to the database
    conn = sqlite3.connect('database.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Define a SQL statement to insert a new row into the user_info table
    sql = "INSERT INTO user_info (username, pass_word) VALUES (?, ?)"

    # Define a tuple of values to insert
    values = (username, password)

    # Execute the statement with the values tuple
    cursor.execute(sql, values)

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username and password are not empty
        if not username or not password:
            flash('Please enter both username and password.')
            return redirect(url_for('register'))
        else:
        # Redirect to a home page
            add_user_to_database(username, password)
            return redirect(url_for('timeline'))
    else:
    # If the request method is GET, return the registration form
        return render_template('register.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # perform validation and authentication here
        # for example, check if username and password match a user in a database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM user_info WHERE username = ? AND pass_word = ?', (username, password))
        user = c.fetchone()

        if user:
            # set the user_id in the session
            session['user_id'] = user[0]

            # redirect to a success page if the user is authenticated
            return redirect(url_for('timeline'))
        else:
            # return an error message if the user is not authenticated
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)
    
    # if the request method is GET, return the login form
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
        # do something with the search results
        return f'Search results for "{search_results}"'
    return render_template('search.html')

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')

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

@app.route('/profile/editProfile')
def edit_profile():
    return render_template('editProfile.html')


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
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/create/', methods=('GET', 'POST'))
def creat():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))

    return render_template('create.html')




if __name__ == '__main__':
    app.run(debug=True)