from flask import Blueprint, render_template, abort, jsonify, request,make_response
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, models, ansible
from utils import ansible


books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


mod = Blueprint('test_api', __name__,
                        template_folder='templates')
# admin_bp = Blueprint('admin_bp', __name__,
#                      template_folder='templates',
#                      static_folder='static')
@mod.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


# example : http://127.0.0.1:4321/api/v1/resources/books?id=2
@mod.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return  make_response(jsonify({'error': 'Not found'}), 404)

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


@mod.route('/api/test/ansible1')
def ansible1():
    #test_add_nodes()
    print("lamtv10")
    runner = ansible.Checker('ansible_compute.yml','multnode',{'extra_vars':{'target':"ta1"} ,'tags':['install','uninstall']},None, False,  None,None,None)
    stats = runner.run()
    return jsonify(ansible.get_stats(stats))


