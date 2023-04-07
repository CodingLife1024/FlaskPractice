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
            return redirect(url_for('home'))
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
            return redirect(url_for('home'))
        else:
            # return an error message if the user is not authenticated
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)
    
    # if the request method is GET, return the login form
    else:
        return render_template('login.html')

@app.route("/popular")
def popular():
    return 'popupal'

@app.route("/timeline")
def timeline():
    return 'timeline'

@app.route("/search")
def search():
    return 'timeline'

@app.route("/profile")
def profile():
    return 'timeline'

@app.route("/create")
def exp():
    return render_template('pop.html')

if __name__ == '__main__':
    app.run(debug=True)