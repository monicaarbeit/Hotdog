from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template("me.html", name=[8, 9, 1])

@app.route('/newpath')
def new_func():
	return render_template("you.html")

@app.route('/')
def echo(msg):
	return 'Your message was: ' + msg

@app.route('/login')
def login():
	return render_template("login.html")

if __name__ == "__main__":
	app.run()