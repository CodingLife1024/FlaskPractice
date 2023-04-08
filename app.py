from flask import Flask, render_template, url_for, flash, redirect, request

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
        
        if username == 'example' and password == 'password':
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

@app.route("/create")
def create():
    return "45345456"

@app.route('/comments', methods=['GET', 'POST'])
def comments():
    return "commmmmm"

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

if __name__ == '__main__':
    app.run(debug=True)