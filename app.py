from flask import Flask, render_template, request, abort
from Ark.ark import Ark
import pprint
pp = pprint.PrettyPrinter(indent=2)


app = Flask(__name__)
app.config.from_pyfile('config.cfg')

ark = Ark()
print(ark.check_token())

@app.route('/',methods=['POST','GET'])
def index():
	if request.method == 'POST':
		if request.form['email'] != '':
			#get and return email things
			email = ark.email(request.form['email'])
			if email == 404:
				abort(404)
			return render_template('person.html',data=email)
		if request.form['handle'] != '':
			#get and return handle things
			twitter = ark.twitter(request.form['handle'])
			if twitter == 404:
				abort(404)
			return render_template('person.html',data=twitter)
	else:
		return render_template('index.html')
	
if __name__ == '__main__':
        app.run()
