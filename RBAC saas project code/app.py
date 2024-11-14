from flask import Flask, render_template, request, redirect, url_for, session
from roles import has_permission

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user database
users = {
    "admin": {"password": "adminpass", "role": "admin"},
    "editor": {"password": "editorpass", "role": "editor"},
    "viewer": {"password": "viewerpass", "role": "viewer"}
}

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Authenticate user
        user = users.get(username)
        if user and user['password'] == password:
            session['username'] = username
            session['role'] = user['role']
            return redirect(url_for('dashboard'))
        
        return "Invalid credentials, please try again" or "user not found !"
                
    return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    role = session.get('role')
    if not role:
        return redirect(url_for('login'))
    
    if not has_permission(role, "view_dashboard"):
        return redirect(url_for('access_denied'))
    
    return render_template('dashboard.html', role=role)

# Access Denied route
@app.route('/access_denied')
def access_denied():
    return render_template('access_denied.html')

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)