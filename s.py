from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>Hooge</h1>"

@app.route('/<username>')
def show_user_profile(username):
	return "<h1>٩(๑>◡<๑)۶ User </br>{}</h1><a href='/'>index</a>".format(username)

@app.route('/login/', methods=['GET', 'POST'])
def logins():
	if request.method == 'POST':
		return "post - Sign in to Kooke"
	else:
		return "get -<form method='post'><input type='submit' value='Submit'></form>"

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "Post %d" % post_id