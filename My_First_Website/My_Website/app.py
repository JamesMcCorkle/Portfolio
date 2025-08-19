"""This is a python program that will open my website using flask"""
from datetime import datetime
import re
from flask import Flask, render_template, request, redirect, url_for, flash, session
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.secret_key = 'b9d2f3c8d2a6e58d4a6b7c9e8d9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f'#hash-32 key

def get_current_datetime():
    """Get Date and Time"""
    return datetime.now().strftime('%m-%d-%y %H:%M:%S')#I prefer the date/time to be formatted this way

users_db = {}

def is_password_complex(password):
    """Check if password meets requirements"""
    if (len(password) >= 12 and#Check for length of 12 chars
        re.search(r'[A-Z]', password) and#Check for a capital letter
        re.search(r'[a-z]', password) and#Check for a lowercase letter
        re.search(r'[0-9]', password) and#Check for a digit
        re.search(r'[\W]', password)):#Finally, check for a special char
        return True
    return False

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Directory for New Users"""
    if request.method == 'POST':
        username = request.form['username']#Request username from user
        password = request.form['password']#Request password for user
        if username in users_db:#Check if an existing user
            flash('Username already exists.')
            return redirect(url_for('register'))
        if not is_password_complex(password):
            flash('Password must be at least 12 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character.')
            return redirect(url_for('register'))
        password_hash = pbkdf2_sha256.hash(password)#encrypt password using sha256
        users_db[username] = password_hash
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """For existing users"""
    if request.method == 'POST':
        username = request.form['username']#Request username from user
        password = request.form['password']#Request password for user
        user = users_db.get(username)#Checks database for provided username and password
        if user and pbkdf2_sha256.verify(password, user):
            session['username'] = username
            flash('Login successful!')
            return redirect(url_for('home'))
        flash('Invalid username or password.')#Handling for invald username/password
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    """For logging out"""
    session.pop('username', None)#logs user out
    flash('You have been logged out.')
    return redirect(url_for('login'))

def login_required(f):
    """Redirects to login to access"""
    def wrap(*args, **kwargs):#checks if user is logged in
        if 'username' not in session:
            flash('You need to log in first.')
            return redirect(url_for('login'))#Redirects user to login page when accessing secured pages while logged out
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap

#Add function/option later to update stats/ranks

@app.route('/')
def home():
    """Home Page"""
    offense_stats = {#Dictionary of general stats for the offense
        'Passing Yards': '2,925',#Stats obtained from ESPN
        'Rushing Yards': '1,223',
        'Total Yards': '4,148',
        'Points Per Game': '30.8'
    }
    defense_stats = {#Dictionary of general stats for the defense
        'Passing Yards Allowed': '1,927',#Stats obtained from ESPN
        'Rushing Yards Allowed': '1,151',
        'Total Yards Allowed': '3,078',
        'Points Allowed Per Game': '18.3'
    }
    current_datetime = get_current_datetime()#Store date/time to a variable for display

    return render_template('Georgia_Home_Page.html', offense_stats=offense_stats, defense_stats=defense_stats,  current_datetime=current_datetime)

@app.route('/offense-rank')
def offense_rank():
    """Offense Rank"""
    offense_rankings = {#Dictionary of major rankings for offense
        'Total Offense': '48th',#Also obtained from espn, has to be updated manually
        'Passing Offense': '11th',
        'Rushing Offense': '102nd'
    }
    current_datetime = get_current_datetime()

    return render_template('Georgia_Offense.html', offense_rankings=offense_rankings,  current_datetime=current_datetime)

@app.route('/defense-rank')
def defense_rank():#Dictionary of major rankings for defense
    """Defense Rank"""
    defense_rankings = {#Ranking obtained from espn
        'Total Defense': '15th',
        'Passing Defense': '36th',
        'Rushing Defense': '29th'
    }
    current_datetime = get_current_datetime()

    return render_template('Georgia_Defense.html', defense_rankings=defense_rankings,  current_datetime=current_datetime)

@app.route('/table')
@login_required
def table():
    """Function for displaying my table"""
    player_data = [
        ['Player', 'Position', 'Yards'],
        ['Carson Beck', 'Quarterback', '3,429'],
        ['Nate Frazeir', 'Running Back', '587'],
        ['Arian Smith', 'Wide Receiver', '709'],
        ['Trevor Etienne', 'Running Back', '477']
    ]
    current_datetime = get_current_datetime()
    return render_template('table.html', data=player_data, current_datetime=current_datetime)

if __name__ == '__main__':
    app.run(debug=True)
