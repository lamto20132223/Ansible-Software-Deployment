import oyaml as yaml
import sys, os
from collections import OrderedDict
# from assets import *
ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
def load_yml_file(file_path):
    with open(file_path) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        result = yaml.load(file, Loader=yaml.FullLoader)

        #print(type(list_task))
    return result


def convert_original_to_input_sf(data, output_file):


    # data = {"ok":"ok"}
    print(data.keys())

    output = []
    default_group = OrderedDict()
    default_group['name'] = 'DEFAULT'
    default_group['configs'] = []
    output.append(default_group)
    for key in data.keys():
        if type(data[key]) is OrderedDict:
            new_group = OrderedDict()
            new_group['name'] = key
            new_group['configs'] = []
            for config in data[key].keys():
                config_data = OrderedDict()
                config_data['key'] = config
                config_data['ex_value'] = data[key][config]
                config_data['required'] = False
                config_data['editable'] = True
                config_data['need_edit'] = False
                config_data['input_type'] = 'text'
                if type(config_data['ex_value']) is int:
                    config_data['input_type'] = 'number'
                if type(config_data['ex_value']) is bool:
                    config_data['input_type'] = 'checkbox'
                new_group['configs'].append(config_data)
            output.append(new_group)
        else:
            config_data=OrderedDict()
            config_data['key'] = key
            config_data['ex_value'] = data[key]
            config_data['required'] = False
            config_data['editable'] = True
            config_data['need_edit'] = False
            config_data['input_type'] = 'text'
            if type(config_data['ex_value']) is int:
                config_data['input_type'] = 'number'
            if type(config_data['ex_value']) is bool:
                config_data['input_type'] = 'checkbox'
            default_group['configs'].append(config_data)


    stream = file(output_file, 'w')
    print(data)
    yaml.dump(output, stream)
def convert_input_sf_to_origin(data, output_file):
    output = OrderedDict()
    for group_data in data:
        if group_data['name']=='DEFAULT':
            for config in group_data['configs']:
                key = config['key']
                value = config['ex_value']
                output[key] =value
        else :
            output[group_data['name']] = OrderedDict()
            for config in group_data['configs']:
                key = config['key']
                value = config['ex_value']
                output[group_data['name']][key] = value
    stream = file(output_file, 'w')
    # print(data)
    yaml.dump(output, stream)
if __name__ == "__main__":
    # data = load_yml_file('./option.yml',)
    # convert_original_to_input_sf(data,'./document.yaml')

    data = load_yml_file('./document2.yaml',)
    convert_input_sf_to_origin(data,'./option2.yml')