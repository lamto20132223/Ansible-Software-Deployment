import numpy as np
import os
def invert_dict(my_dict):
	return dict(map(reversed, my_dict.items()))
	#{"red":"do", "blue":"xanh", "yellow":"vang"} ---> {"do":"red", "xanh":"blue", "vang":"yellow"}

def sum_element_in_2_list(list1, list2):
	return np.add(list1, list2)
	#[1,2,3]+[2,3,4]=[3,5,7]

def isfile(path):
	return os.path.isfile(path)

def merge_2_list_into_1_dict(list1,list2):
	return  dict(zip(list1, list1))

def clone_list(my_list):
	return list(my_list)

def sort_list_string(my_list):
	return sorted(my_list,reverse=True)
#
# def sort_list_dict(my_list):
# 	return sorted(csv_mapping_list, key=lambda item: item.get("Age"))

def comprehension_list(my_list):
	return [2 * item for item in my_list if item < 0]
	# Duplicate, filter, and scale a 1D list of constants

def merge_dict(dict1,dict2):
	powers = dict1.copy()
	powers.update(dict2)
	return powers

def print_join(log1, log2):
	print(''.join(["log1 is ", str(log1), ", log2 is ", str(log2), " end!"]))

##task = [task for task in tasks if task['id'] == task_id]

#curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
#curl -X POST "http://172.16.29.193:9876/language" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"file\": \"docker.io/istio/sidecar_injector:1.4.4\"}"


def get_secret_key():
	return os.urandom(24)