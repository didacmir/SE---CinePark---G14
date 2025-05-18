from flask import Flask, render_template, request, redirect, url_for
from auth import register_user, verify_login

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        identifier = request.form['username']
        password = request.form['password']
        if verify_login(identifier, password):
            return render_template('dashboard.html', username=identifier)
        else:
            error = "⚠️ Invalid username/email or password."
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        result = register_user(username, email, password)
        if result == "success":
            return redirect(url_for('login'))
        else:
            error = f"⚠️ {result}"
    return render_template('signup.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
