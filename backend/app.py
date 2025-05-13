from flask import Flask, render_template, request, redirect, url_for
from auth import register_user, verify_login

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form['username']
        password = request.form['password']
        if verify_login(identifier, password):
            return render_template('dashboard.html')
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        result = register_user(username, email, password)
        if result == "success":
            return redirect(url_for('login'))
        else:
            return result, 400
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
