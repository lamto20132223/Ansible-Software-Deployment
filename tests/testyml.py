import oyaml as yaml
import os
import sys
def load_yml_file(file_path):

    with open(file_path) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        result = yaml.load(file, Loader=yaml.FullLoader)

        #print(type(list_task))
    return result

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)

list_tasks = load_yml_file(ROOT_DIR +  '/main.yml')
list_tasks2= [task for task in list_tasks if task.get('include') == None]

print(load_yml_file(ROOT_DIR +  '/main.yml'))

