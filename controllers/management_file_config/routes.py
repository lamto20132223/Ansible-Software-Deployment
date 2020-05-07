from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *

mod = Blueprint('management_file_config', __name__,
                        template_folder='templates')








# def convert_cfg_to_yaml():
#     return "INCOMMING"
#
# def convert_yaml_to_cfg():
#     return "INCOMMING"
#
#
# def add_file_config_to_manager():
#
#
# def list_all_file_config():
#     get,set,download
#
# def edit_one_file_config():




@mod.route('/configs/<string:host_id>', methods=['GET'])
def get_all_config_in_host(host_id):
    return "INCOMMING"

@mod.route('/configs/filter', methods=['GET'])
def search_file_config():
    if not (request.args.get('name') and request.args.get('path') and request.args.get('node') and request.args.get('service')):
        abort(400)
    return "INCOMMING"


@mod.route('/configs/download_configs', methods=['POST'])
def download_file_config():
    if not request.json :
        abort(400)
    else:
        data = request.json

    return "INCOMMING"

@mod.route('/configs/compare_config_db_vs_host', methods=['GET'])
def compare_config_db_vs_host():
    if not (request.args.get('host_id')) or not (request.args.get('file_config_id')):
        abort(400)
    return "INCOMMING"

@mod.route('/configs/compare_config_db_vs_db', methods=['GET'])
def compare_config_db_vs_db():
    if not (request.args.get('file_config_1_id') and request.args.get('file_config_1_id')):
        abort(400)
    return "INCOMMING"

@mod.route('/configs/compare_config_host_vs_host', methods=['GET'])
def compare_config_host_vs_host():
    if not (request.args.get('file_config_1_id') and request.args.get('file_config_2_id') ):
        abort(400)
    return "INCOMMING"


@mod.route('/configs/<string:file_config_id>', methods=['GET'])
def get_file_config_content():
    return "Lay ra noi dung cua File_config ID"

@mod.route('/configs/<string:file_config_id>/services', methods=['GET'])
def get_list_services_related_to_file_config():
    return "Lay danh sach service dang su dung file_config"

@mod.route('/configs/<string:file_config_id>/content', methods=['GET'])
def get_file_config_content_with_type():
    if not (request.args.get('type')):
        abort(400)
    return " Lay ra noi dung file_config theo type de so sanh voi nhau + database: dang o trong database + server: Noi dung thuc te tren server + lastupdate: Noi dung truoc khi commit, update"






@mod.route('/configs/update', methods=['POST'])
def update_file_config_from_db_server():
    if not (request.args.get('file_config_id')):
        abort(400)
    return "Update File Config From DB to Server"



@mod.route('/configs/commit', methods=['POST'])
def update_file_config_from_server_to_server():
    if not (request.args.get('file_config_id')):
        abort(400)
    return "Update File Config From DB to Server"

@mod.route('/configs/rollback', methods=['POST'])
def rollback_file_config():
    if not (request.args.get('file_config_id')):
        abort(400)
    return "Update File Config From DB to Server"




@mod.route('/tests/test1')
def rest_assurate_test():
    jsonx = {
        "lotto":{
         "lottoId":5,
         "winning-numbers":[2,45,34,23,7,5,3],
         "winners":[{
           "winnerId":23,
           "numbers":[2,45,34,23,3,5]
         },{
           "winnerId":54,
           "numbers":[52,3,12,11,18,22]
         }]
        }
        }

    return jsonx,200


@mod.route('/tests/test2')
def rest_assurate_test2():
    jsonx = {
   "store":{
      "book":[
         {
            "author":"Nigel Rees",
            "category":"reference",
            "price":8.95,
            "title":"Sayings of the Century"
         },
         {
            "author":"Evelyn Waugh",
            "category":"fiction",
            "price":12.99,
            "title":"Sword of Honour"
         },
         {
            "author":"Herman Melville",
            "category":"fiction",
            "isbn":"0-553-21311-3",
            "price":8.99,
            "title":"Moby Dick"
         },
         {
            "author":"J. R. R. Tolkien",
            "category":"fiction",
            "isbn":"0-395-19395-8",
            "price":22.99,
            "title":"The Lord of the Rings"
         }
      ]
   }
}

    return jsonx,200



@mod.route('/tests/test3')
def rest_assurate_test3():
    jsonx = [
          {
              "id": 2,
              "name": "An ice sculpture",
              "price": 12.50,
              "tags": ["cold", "ice"],
              "dimensions": {
                  "length": 7.0,
                  "width": 12.0,
                  "height": 9.5
              },
              "warehouseLocation": {
                  "latitude": -78.75,
                  "longitude": 20.4
              }
          },
          {
              "id": 3,
              "name": "A blue mouse",
              "price": 25.50,
                  "dimensions": {
                  "length": 3.1,
                  "width": 1.0,
                  "height": 1.0
              },
              "warehouseLocation": {
                  "latitude": 54.4,
                  "longitude": -32.7
              }
          }
      ]
    return jsonify(jsonx),200




@mod.route('/tests/test5', methods = ['GET', 'POST'])
def rest_assurate_test5():
    if request.method== 'POST':
        jsonx = request.json
        return jsonify(jsonx),200
    else:
        json = {'message':'Hello From Flask'}
        return jsonify(json), 200




