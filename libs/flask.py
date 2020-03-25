flask-restplus
flask-sqlalchemy
flask-migrate 
flask-praetorian 
flask-sessions cho user session management
flask-login cho manage user login 




- flask-debugtoolbar: hỗ trợ một tollbar show HTTP headers, request variables, config settings.
- pytest and pyest-cov: Sử dụng để test Flask applications.
- flake8
- flask-sqlalchemy 
- alembic: migrate database 
- celery and redis: Running 1 off tasks or scheduled tasks. 
- Flask-WTF and WTForms-Components: Process Forms, set up validation rules and additional logic related to processing a form. Vi du: TimeField, SelectMultipleField tuong tuong co mot username field khi bạn muốn cho đảm bảo no duplicates exist WTForms-Components là perfect.
- Flask-login + Flask-Security 
- Flask-limiter: 

# scp -r Anaconda2....
# conda create -n flask-app
# conda activate flask-app
# conda install python==2.7
# python
# conda install -c anaconda flask
# conda install -c conda-forge flask-restplus
# conda install -c conda-forge ansible
# conda install -c anaconda configparser
# conda install -c anaconda sqlalchemy
# conda install -c conda-forge flask-sqlalchemy
# conda install -c anaconda numpy
# conda info
# scp -r /root/anaconda2/envs/flask-app root@172.16.29.194:/root/anaconda2/envs/
#
# y


Thêm một vòng for truy vấn vào tất cả các file có trong thư mục controller lấy ra các request trong đó convert to .... /route/...

https://www.youtube.com/watch?v=yh-28ksEXwY&list=PLNrnt5k3GHOO8kB6vKenpAWvZuvVQiHro



flask@api:



app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')

@app.route("/")
def hello():
    headers = {"Content-Type": "application/json"}
    return make_response('it worked!', 200, headers)


- Router cho xác định xem user sẽ được phục vụ gì khi truy cập vào URL bên trong app. 
- Form classes là Python models xác định data mà forms của chúng ta sẽ bắt cũng như logic cho validating khi nòa hoặc không usert hoàn thành 1 form (đặt trong forms.py)
- template render HTML 


...
class ContactForm(FlaskForm):
	name = StringField('Name', [
        DataRequired()])
    email = StringField('Email', [
        Email(message=('Not a valid email address.')),
        DataRequired()])
    body = TextField('Message', [
        DataRequired(),
        Length(min=4, message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

@app.route('/', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('index.html', form=form)






a_language = api.model('Language', {'language': fields.String('The language.')})
# tuyên bố model mà API có thể serialize

@api.route('/language')
@api.marshal_with(a_language):
	Một decorator apply marshalling vào phần return value của methods 
	ví dụ 

mfields = { 'a': fields.Raw }
>>> @marshal_with(mfields)
... def get():
...     return { 'a': 100, 'b': 'foo' }
...
...
>>> get()


@api.expect(a_language)
# chi dinh expected input fields. Nó accepts một optional boolean parameter validate indicating whether the payload should be validated. 

app.config['RESTPLUS_VALIDATE'] = True

api = Api(app)

resource_fields = api.model('Resource', {
    'name': fields.String,
})

@api.route('/my-resource/<id>')
class MyResource(Resource):
    # Payload validation enabled
    @api.expect(resource_fields)
    def post(self):
        pass

    # Payload validation disabled
    @api.expect(resource_fields, validate=False)
    def post(self):
        pass



@api.response():
Document known response 


@api.route('/my-resource/')
class MyResource(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    def get(self):
        pass


@api.route('/my-resource/')
class MyResource(Resource):
    @api.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def get(self):
        pass



******************
@api.header('X-Header', 'Some class header')









----------------- Su dung ket hop Flask voi Blueprints:
app.py: entry point 
models.py: database models 
config.py: config. 


-  Đăng ký một kế hoạch chi tiết trên một ứng dụng với tiền tố URL và / hoặc tên miền phụ. Các tham số trong tiền tố URL / tên miền phụ trở thành đối số xem phổ biến (có mặc định) trên tất cả các chức năng xem trong kế hoạch chi tiết.
- Dang ky mot blueprint nhieu lan tren mot ung dung voi cac URL rules khac nhau
- Cung cap template filters, static files, templates, cac utilities thong qua blueprints. Mot blueprint khong nhat thiet phai implement application hoac view funtions
-




https://hackersandslackers.com/flask-blueprints

flaskblueprint-tutorial
├── /application
│   ├── __init__.py
│   ├── /admin
│   │   ├── __init__.py
│   │   ├── admin_routes.py
│   │   ├── assets.py
│   │   └── /templates
│   ├── /main
│   │   ├── __init__.py
│   │   ├── assets.py
│   │   ├── main_routes.py
│   │   └── /templates
│   ├── /static
│   └── /templates
│       ├── layout.html
│       ├── meta.html
│       ├── navigation-default.html
│       ├── navigation-loggedin.html
│       └── scripts.html
├── config.py
├── requirements.txt
├── start.sh
└── wsgi.py



from flask import Flask
from yourapplication.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)
app.register_blueprint(simple_page, url_prefix='/pages')

>>> simple_page.root_path
'/Users/username/TestProject/yourapplication'

with simple_page.open_resource('static/style.css') as f:
    code = f.read()


-----
Art of Routing in Flask 
- 
Xảy ra khi applications are a medium for data such as user-generated content such as user profiles or author posts, and routes simply define the way our users will access data which is always changing. 
==> Define dynamic routing opportunities which can potentially grow endlessly. 


HTTP Methods:
	- @app.route('/api/v1/users', methods=['GET', 'POST', 'PUT'])
Route Variable Rules:
	- @app.route('/user/<username>')
		def profile(username):
	- @app.route('/<int:year>/<int:month>/<title>') # type-checked variables co 4 loai: string, int, float, path
		def article(year, month, title):

Make a response object:

	- Su dung make_response() cho phep chung ta server up information khi dong thoi cung cap status code (200 hoac 500) va cho phep chung ta bo xung headers vao response. 

	from flask import Flask, make_response
	app = Flask(__name__)

	@app.route("/api/v2/test_response")
	def users():
	    headers = {"Content-Type": "application/json"}
	    return make_response('Test worked!',
	                         200,
	                         headers=headers)



Redirecting Users 
Request Object:
	- request.method: Chứa method được sử dụng để truy cập vào route như là GET hoặc POST, chúng ta sử dụng logic này để có một route phục vụ nhiều responses dựa trên method được sử dụng để gọi route. ví dụ if request.method=='POST' có thể mở một block chỉ thực thi POST request trong route 
	- request.args: Chứa query-string parameters của một request hit our route. Ví dụ   if request.args.get('url').
	- request.data: trả về body của một object posted to route 
	- request.form: Cách access vào information form posted ví dụ if request.form['username']
	- request.headers: Chứa headers của một request 

...

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    """User sign-up page."""
    signup_form = SignupForm(request.form)
    # POST: Sign user in
    if request.method == 'POST':
        if signup_form.validate():
            # Get Form Fields
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            website = request.form.get('website')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(name=name,
                            email=email,
                            password=generate_password_hash(password, method='sha256'),
                            website=website)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('main_bp.dashboard'))
            flash('A user already exists with that email address.')
            return redirect(url_for('auth_bp.signup_page'))
    # GET: Serve Sign-up page
    return render_template('/signup.html',
                           title='Create an Account | Flask-Login Tutorial.',
                           form=SignupForm(),
                           template='signup-page',
                           body="Sign up for a user account.")





---------
The g Object:
from flask import g 

def get_test_value():
	if 'test_value' not in g:
		g.test_value = 'This is a value'
	return 

from flask import g


@app.teardown_testvalue
def remove_test_value():
   test_value = g.pop('test_value', None)




************************** CONFIG FLASK APP ***************************
https://hackersandslackers.com/configure-flask-applications

app.config.from_pyfile('application.cfg',
                       silent=True)          # Config from cfg file


"""Flask config class."""
import os


class Config:
    """Base config vars."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')



app.config.from_object('config.Config')  

*********************** FLASK _SQL _ALCHEMY *******************

SQLALCHEMY_DATABASE_URI: Connection string of your app's database 
SQLALCHEMY_ECHO: Prints database-related actions to console for debugging purposes 
SQLALCHEMY_ENGINE_OPTIONS: Additional options to be passed to SQLAlchemy engine with hold your app's database connection 



Flask-Session:
- SESSION_TYPE: redis, memcached, filesystem, mongodb 



Muc tieu cua flask-sqlalchemy la tuong tac giua Flask:
- tao configures engine
- tao connection va session


ask_SQLAlchemy handles session configuration, setup and teardown for you.
Gives you declarative base model that makes querying and pagination easier
Backend specific settings.Flask-SQLAlchemy scans installed libs for Unicode support and if fails automatically uses SQLAlchemy Unicode.
Has a method called apply_driver_hacks that automatically sets sane defaults to thigs like MySQL pool-size
Has nice build in methods create_all() and drop_all() for creating and dropping all tables. Useful for testing and in python command line if you did something stupid
It gives you get_or_404()instead of get() and find_or_404() instead of find() Code example at > http://flask-sqlalchemy.pocoo.org/2.1/queries/







#######################################################################################################################
*************************************  ANACONDA ********************************************************************

*********************************************************************************************************************
*********************************************************************************************************************
*********************************************************************************************************************
*********************************************************************************************************************
########################################################################################################################

(viettel) [root@controller01 ~]# cat ~/anaconda2/envs/viettel/conda-meta/history | grep '# cmd' | cut -d" " -f3-

/home/lamtv10/anaconda2/envs/
cat /home/lamtv10/anaconda2/envs/viettel/conda-meta/history | grep '# cmd' | cut -d" " -f3-


conda create -n viettel python=2.7
conda install -c anaconda numpy
conda install -c anaconda flask
conda install -c anaconda pymysql
conda install -c conda-forge flask-restplus
conda install -c conda-forge ansible
conda install -c anaconda configparser
conda install -c anaconda sqlalchemy
conda install -c conda-forge flask-sqlalchemy
conda install -c conda-forge flask-migrate
conda install -c anaconda flask-login
conda install -c conda-forge pytest
conda install -c conda-forge flask-wtf
conda install -c conda-forge packaging
conda install -c conda-forge fabric
conda install -c anaconda redis
conda install -c anaconda redis-py
conda install PyYAML
conda install pyOpenSSL
conda install flake8
conda install -c conda-forge flask-marshmallow
conda install -c conda-forge marshmallow-sqlalchemy
pip install ansible==2.7.4
pip install Werkzeug==0.16.1
conda install oyaml





conda deactivate
conda remove --name viettel --all
cd /home/vttek/anaconda2/envs/
scp -r root@172.16.29.193:/home/lamtv10/anaconda2/envs/viettel/ ./
conda info --envs
conda acitvate viettel





====== ansible runner service
https://github.com/ansible/ansible-runner-service


wraps ansible_runner interface inside REST API enable ansible playbooks to be executed and queried from other platforms
- expose playbooks by name found within project folder
- supports Ansible environment
- playbook can run with tags to change execution behavior
- playbook can use limit to restrict action to a specific host
- playbooks can use check parameter to run ansible in check mode
(((Check mode vô cùng hữu ích cho việc test code hoặc abc ,,,,)))
Ví dụ: ansible-playbook foo.yml --check

- running playbook may be cancelled
- support execution of concurrent playbook
- playbook state shows overall status, with current active task name
- events may be filtered for specific output e.g. ?task=RSEULTS to show events with a taskname of RESULTS
-

+++ Inventory management :
    - hosts and groups được quản lý thông qua API /groups and API /hosts endpoints
    - trước khi host có thể được thêm vào inventory, nó được checked cho dns và passwordless ssh
    - cung cấp một /api endpoints mô tả tất cả  endpoints
        mỗi description mô tả một curl command example, together với output
    - Query the state or cancel the ansible run
    -



API Route   Description
/api    Show available API endpoints (this page)
/api/v1/groups  List all the defined groups in the inventory
/api/v1/groups/<group_name> Manage groups within the inventory
/api/v1/groupvars/<group_name>  Manage group variables
/api/v1/hosts   Return a list of hosts from the inventory
/api/v1/hosts/<host_name>   Show group membership for a given host
/api/v1/hosts/<host_name>/groups/<group_name>   Manage ansible control of a given host
/api/v1/hostvars/<host_name>/groups/<group_name>    Manage host variables for a specific group within the inventory
/api/v1/jobs/<play_uuid>/events Return a list of events within a given playbook run (job)
/api/v1/jobs/<play_uuid>/events/<event_uuid>    Return the output of a specific task within a playbook
/api/v1/playbooks   Return the names of all available playbooks
/api/v1/playbooks/<play_uuid>   Query the state or cancel a playbook run (by uuid)
/api/v1/playbooks/<playbook_name>   Start a playbook by name, returning the play's uuid
/api/v1/playbooks/<playbook_name>/tags/ Start a playbook using tags to control which tasks run
/metrics    Provide prometheus compatible statistics which describe playbook activity





-logging.yaml
-config.yaml
-certs:
    + client
    + server
-artifacts
-inventory
-env
-project
    + roles
    + library
    + test.yaml
-roles












############ remove pycharm underline
https://www.youtube.com/watch?v=0Du9fwdUIeY

mysql - u root < test.sql

USE `auto_lamtv10` ;
DELETE FROM changes;
DELETE FROM  deployments;
DELETE FROM  disk_resources;
DELETE FROM  file_configs;
DELETE FROM  interface_resources;
DELETE FROM  node_infos;
DELETE FROM  node_roles;
DELETE FROM  nodes;
DELETE FROM  openstack_configs;
DELETE FROM  passwords;
DELETE FROM  service_info_file_config;
DELETE FROM  service_infos;
DELETE FROM  service_setups;
DELETE FROM  tasks;
DELETE FROM  update_change;
DELETE FROM  updates;

