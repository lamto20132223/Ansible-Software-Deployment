from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')
# admin_bp = Blueprint('admin_bp', __name__,
#                      template_folder='templates',
#                      static_folder='static')
@simple_page.route('/')
def hello():
    return 'helo'
@simple_page.route('/lamtv10')
def lamtv10():
    return 'lamtv10'

@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)