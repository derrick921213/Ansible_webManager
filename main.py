import os
from simplepam import authenticate
from flask import Flask, session,redirect,url_for,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        user_title = list(session['username'])[0].upper()
        return render_template('starter.html',user_title=user_title)
    return redirect(url_for('login'))


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(str(username),str(password)):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='True')