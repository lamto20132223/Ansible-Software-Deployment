@app.route('/user/<username>')
def profile(username):
    ...

@app.route('/<int:year>/<int:month>/<title>')
def article(year, month, title):
    ...

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
GET:
example.com?arg1=value1&arg2=value2

http://127.0.0.1:5000/query-example?language=Python



====> request.args.get('language') or request.args['language']

@app.route('/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None

    return '''<h1>The language value is: {}</h1>'''.format(language)


POST:
@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

#########################################################################################################
req_data = request.get_json()

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()

    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
    example = req_data['examples'][0] #an index is needed because of the array
    boolean_test = req_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)






string: Accepts any text without a slash (the default).
int: Accepts integers.
float: Accepts numerical values containing decimal points.
path: Similar to a string, but accepts slashes.



RETURN +++++++++++++++++++


def hello():
    return Markup("<h1>Hello World!</h1>")

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from flask import Flask, render_template
app = Flask(__name__,
            template_folder="templates")

@app.route("/")
def home():
    """Serve homepage template."""
    return render_template('index.html',
                           title='Flask-Login Tutorial.',
                           body="You are now logged in!")

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from flask import Flask, make_response, request, jsonify
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    my_dict = {'key': 'dictionary value'}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(my_dict), 200, headers)




++++++++++++++++++++++++++++++++++++++++++++++++++++


from flask_restplus import Api, Resource

mod_v1 =Api(mod, version='1.0', title='Todo API',
    description='A simple TODO API',
)


@mod_v1.route('/roles', methods=['GET','POST'])
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}






