from flask import Flask
app=Flask(__name__)
# import site
# import api
from ss.index import index_blueprint
#from site.routes import index_blueprint
#
app.register_blueprint(index_blueprint)
# app.register_blueprint(api_mod, url_prefix='/api')

#
# @app.route('/getStuff')
# def getStuff():
#     return  '{"result" : "you are in the api !!!"}'
# @app.route('/')
# def homepage():
#     return '<h1>You are on the home page !!!! </h1>'
app.run(debug=True)