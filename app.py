from flask import Flask, render_template, request, redirect, url_for, session

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

# Dummy credentials
USERNAME = "mohamad"
PASSWORD = "123456"

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == USERNAME and password == PASSWORD:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    
    return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    return redirect(url_for('login'))

# New routes for Home, CRM, and Agriculture Management
@app.route('/home')
def home():
    if 'user' in session:
        return "<h1>Home Page</h1><p>Welcome to the Home Page!</p>"
    return redirect(url_for('login'))

@app.route('/crm')
def crm():
    if 'user' in session:
        return "<h1>CRM</h1><p>Welcome to the CRM Section!</p>"
    return redirect(url_for('login'))

@app.route('/agriculture')
def agriculture():
    if 'user' in session:
        return "<h1>Agriculture Management</h1><p>Manage agriculture operations here.</p>"
    return redirect(url_for('login'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

