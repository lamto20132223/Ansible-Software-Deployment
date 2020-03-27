from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from multiprocessing import Process
import  os
import time
from multiprocessing.pool import ThreadPool
mod = Blueprint('test_thread', __name__,
                        template_folder='templates')
# admin_bp = Blueprint('admin_bp', __name__,
#                      template_folder='templates',
#                      static_folder='static')


@mod.route('/')
def hello():
    return 'helo'
@mod.route('/lamtv10')
def lamtv10():
    return 'lamtv10'

@mod.route('/<page>')

def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)

def foo(bar, baz,wa):
    print 'hello {0}'.format(bar)
    time.sleep(wa)
    return 'foo' + baz
pool=None
@mod.route('/thread1')
def thread1():
    pool = Process(target=foo, args=('world', 'foo1', 5))
    pool.start()
    pool.join()


    return_val = str(pool.is_alive())
    return return_val

@mod.route('/thread2')
def thread2():
    pool.terminate()
    return_val = "ok"
    return return_val


@mod.route('/thread3')
def thread3():

    return_val = "pool " + str(pool.is_alive())
    return return_val