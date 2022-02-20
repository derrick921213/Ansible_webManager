import re
from simplepam import authenticate
from flask import Flask, session,redirect,url_for,escape,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s <p><a href="%s" target="_self">Logout</a></p>' % (escape(session['username']),'/logout')
    return redirect(url_for('login'))

@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(str(username),str(password)):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug='True')