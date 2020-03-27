from flask import Blueprint
mod = Blueprint('api', __name__)

@mod.route('/getStuff')
def getStuff():
    return  '{"result" : "you are in the api !!!"}'