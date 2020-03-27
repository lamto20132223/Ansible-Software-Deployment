from flask import Flask

import importlib


simple_page = importlib.import_module('views.index')

app=Flask(__name__)
# import site
# import api

sp='simple_page'
#from views.index  import simple_page
#
app.register_blueprint(simple_page['simple_page'])
#app.register_blueprint(api_mod, url_prefix='/api')

#
@app.route('/getStuff')
def getStuff():
    return  '{"result" : "you are in the api !!!"}'
# @app.route('/')
# def homepage():
#     return '<h1>You are on the home page !!!! </h1>'
app.run(debug=True)