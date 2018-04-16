from flask import Flask, request, render_template, make_response, url_for, redirect, abort, escape, session

app = Flask(__name__)

@app.route('/')
def index():
#	username = request.cookies.get('username')
#	return "<h1>Hooge</h1>"
#	return render_template('index.html', username=username)
#	resp = make_response(render_template('index.html'))
#	resp.set_cookie('username', 'username k')
#	return resp
#	return redirect(url_for('cookie'))
#	abort(404)

#	if 'username' in session:
#		return 'Logged in as %s' % escape(session['username'])
#	return 'You are not logged in'
#	return request.headers.get('Connection')
	return render_template('index.html')
app.secret_key ='\xa5/\x9dC\xf2\xd0,\xae\xb4\xb15\x85\x02a\xa7\x8c\x0fx\xd1)\x86\x8f&\x92'

@app.route('/404')
def page_not_found():
	abort(404)
	
@app.route('/<username>')
def show_user_profile(username=None):
	return render_template('user.html', username=username)

@app.route('/login/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] == 'c' and request.form['password'] == 'hooge':
			return request.form['username'] + ' login successful!'
		else:
			error = 'Invalid username/password'
	return render_template('login.html', error=error)
#		return "post - Sign in to Kooke"
#	else:
#		return "get -<form method='post'><input type='submit' value='Submit'></form>"

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "Post %d" % post_id

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['the_file']
		f.save('e:\\uploaded_file.txt')
	else:
		return render_template('upload.html')

@app.route('/cookies')
def kcookie():
	return request.cookies.get('username')

@app.errorhandler(404)
def page_not_found(error):
	resp = make_response(render_template('error.html'), 404)
	resp.headers['X-Something'] = 'A value'
	return resp

if __name__ == '__main__':
#	app.run(debug=True, host='0.0.0.0')
#	print(app.view_functions)
#	print(app.url_map)
#	print(app.url_map._rules)
	print(app.url_map._rules_by_endpoint)