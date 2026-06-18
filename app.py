from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your-secret-key-change-this'

db = SQLAlchemy(app)

# Generate or load encryption key
KEY_FILE = 'secret.key'

def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
        return key

ENCRYPTION_KEY = load_or_create_key()
cipher = Fernet(ENCRYPTION_KEY)

# Database Model
class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    encrypted_password = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def decrypt_password(self):
        return cipher.decrypt(self.encrypted_password.encode()).decode()

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    passwords = Password.query.all()
    return render_template('index.html', passwords=passwords)

@app.route('/add', methods=['GET', 'POST'])
def add_password():
    if request.method == 'POST':
        website = request.form.get('website')
        username = request.form.get('username')
        password = request.form.get('password')

        if not website or not username or not password:
            flash('All fields are required!', 'error')
            return redirect(url_for('add_password'))

        # Encrypt password
        encrypted_pwd = cipher.encrypt(password.encode()).decode()

        # Save to database
        new_password = Password(
            website=website,
            username=username,
            encrypted_password=encrypted_pwd
        )
        db.session.add(new_password)
        db.session.commit()

        flash(f'Password for {website} saved successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_password.html')

@app.route('/view/<int:id>')
def view_password(id):
    password = Password.query.get_or_404(id)
    decrypted_pwd = password.decrypt_password()
    return render_template('view_password.html', password=password, decrypted_pwd=decrypted_pwd)

@app.route('/delete/<int:id>')
def delete_password(id):
    password = Password.query.get_or_404(id)
    db.session.delete(password)
    db.session.commit()
    flash('Password deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    if query:
        passwords = Password.query.filter(
            Password.website.contains(query) | Password.username.contains(query)
        ).all()
    else:
        passwords = Password.query.all()
    return render_template('index.html', passwords=passwords, search_query=query)
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)