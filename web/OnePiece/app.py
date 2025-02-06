# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'onepiece-secret-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, password_hash, character_name):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.character_name = character_name

# Static user credentials
users = {
    1: User(
        id=1,
        username="luffy",
        password_hash=generate_password_hash("strawhat"),
        character_name="Monkey D. Luffy",
    ),
    2: User(
        id=2,
        username="robin",
        password_hash=generate_password_hash("asifbvlf46546484123!@#$%^&*bvdaskljhbfvdjh"), #The should not login
        character_name="Nico Robin",
    )
}

# Username to ID mapping for lookup
username_to_id = {user.username: user_id for user_id, user in users.items()}

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user_id = username_to_id.get(username)
        if user_id is None:
            flash('Invalid username or password')
            return render_template('login.html')
            
        user = users[user_id]
        if check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('can_read_poneglyph', None)  # Clear poneglyph session
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        password = request.form.get('password')
        if password:
            flash("Incorrect Password")
        
        
        username = request.form.get('username')
        if username:
            flash(f"Here is ur secert path to access : /unlock/{username.encode("utf-8").hex()}")
    return render_template('dashboard.html', character_name=current_user.character_name)


@app.route('/unlock/<key>', methods=['GET'])
@login_required
def unlock(key):
    try:
        username = bytes.fromhex(key).decode('utf-8')
    except:
        return "Invalid Access!"
    user_id = username_to_id.get(username)
    if user_id is None:
        return "You are not vaild user"
    if user_id == 1:
        return render_template('clue.html')
    elif user_id == 2:
        return render_template('decoded_message.html')
if __name__ == '__main__':
    app.run()