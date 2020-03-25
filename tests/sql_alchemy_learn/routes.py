from sql_alchemy_learn import app


@app.route("/")
def home():
    return "Hello World!"


@app.route('/index')
def index():
    return "Hello, World!"