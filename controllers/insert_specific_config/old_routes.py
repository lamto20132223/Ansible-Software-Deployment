from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *




from flask_restplus import Api, Resource

mod = Blueprint('insert_specific_config', __name__,
                        template_folder='templates')

mod_v1 =Api(mod, version='1.0', title='Todo API',
    description='A simple TODO API',
)



@mod_v1.route('/configs/specific_configs', methods=['GET', 'POST' , 'PUT'])
class Specific_Configs(Resource):
    def get(self):
        return { "status": "Got new data" }
    def post(self):
        return { "status": "Posted new data" }
    def put(self):
        return { "status": "Posted new data" }


@mod.route('/configs/specific_configs/validate', methods=['POST'])
def validate_specific_config():
    if not request.json :
        abort(400)
    else:
        data = request.json
    return "INCOMMING"


@mod.route('/configs/specific_configs/recommend', methods=['GET'])
def get_recommend_config():
    if not (request.args.get('config_key') and request.args.get('config_value')):
        abort(400)

    return "INCOMMING"


@mod.route('/configs/specific_configs/submit', methods=['POST'])
def submit_configs():
    if not request.json:
        abort(400)
    else:
        data = request.json
    return "INCOMMING"


@mod_v1.route('/configs/specific_configs', methods=['GET', 'POST' , 'PUT'])
class Specific_Configs(Resource):
    def get(self):
        return { "status": "Got new data" }
    def post(self):
        return { "status": "Posted new data" }
    def put(self):
        return { "status": "Posted new data" }







from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextField
from wtforms.validators import DataRequired,Email,Length
class ContactForm(FlaskForm):
    """Contact form."""

    list_Field=[]
    name = StringField('First name', [
        DataRequired()])
    email = StringField('Email', [
        Email(message=('Not a valid email address.')),
        DataRequired()])
    body = TextField('Message', [
        DataRequired(),
        Length(min=4, message=('Your message is too short.'))])

    submit = SubmitField('Submit')
# @mod.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Sign In', form=form)

@mod.route('/contact', methods=('GET', 'POST'))
def contace():
    form = ContactForm()

    print(len(form.list_Field))
    if form.validate_on_submit():
        print(form.name.data + form.email.data + form.body.data)
        return {"ok" :"ok"}
    return render_template('contact.html', form=form)


@mod.route('/form', methods=('GET', 'POST'))
def form():
    # form = ContactForm()
    #
    # name = StringField('First name', [DataRequired()])
    # print(type(name))
    # form.list_Field.append(name)
    #
    #
    # print(len(form.list_Field))
    # print(type(form.list_Field[0]))
    #
    # if form.validate_on_submit():
    #     print(form.name.data + form.email.data + form.body.data)
    #     return {"ok": "ok"}

    my_fields = [
        {
            "label": "First name",
            "name": "name"
        },
        {
            "label": "Second hand",
            "name": "second"
        }
    ]

    print request.method

    if request.method == 'POST':
        print (request.form.get("second"))

    return render_template('form.html', my_fields=my_fields)


@mod.route('/contact2')
def login2():
    if not request.json :
        abort(400)

    return {"ok":json.dumps(request.json)}