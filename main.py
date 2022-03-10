import os
from flask import Flask, session,redirect,url_for,request,render_template
from Utils.account import canLogin

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        user_title = list(session['username'])[0].upper()
        return render_template('starter.html',user_title=user_title,username=session['username'])
    return redirect(url_for('login'))


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        method = request.form['method']
        if canLogin(str(username),str(password), 'web_manager' if 'admin' in str(method) else False):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='True')