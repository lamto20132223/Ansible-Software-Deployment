import json
import ast
import logging
from collections import OrderedDict
import re
info = "{'msg' : 'm OK'}"

info = "OrderedDict([('controller01', '172.16.29.194'), ('controller02', '172.16.29.193'),('controller03', '172.16.29.193'),('compute01', 'compute01'), ('compute02','compute02'), ('compute03', 'compute03')])"

print(type(info))
if re.match(r'^OrderedDict\((.+)\)$', str(info)):
    info = eval( str(info), {'OrderedDict': OrderedDict})

print(type(info))

a = eval(info, {'OrderedDict': OrderedDict})
print (a)
print(type(a))
x = json.dumps( ast.literal_eval(info))
print(type(x))



log = " {'msg': u'All items completed', 'failed': True, 'changed': True, 'results': [{'stderr_lines': [], 'ansible_loop_var': u'item', u'end': u'2020-04-01 05:32:08.107605', 'failed': False, u'stdout': u'172.16.29.23     ', u'changed': True, u'rc': 0, 'item': u'echo \"172.16.29.23     \"', u'cmd': [u'echo', u'172.16.29.23     '], u'stderr': u'', u'delta': u'0:00:00.002855', u'invocation': {u'module_args': {u'creates': None, u'executable': None, u'_uses_shell': False, u'strip_empty_ends': True, u'_raw_params': u'echo \"172.16.29.23     \"', u'removes': None, u'argv': None, u'warn': True, u'chdir': None, u'stdin_add_newline': True, u'stdin': None}}, 'stdout_lines': [u'172.16.29.23     '], u'start': u'2020-04-01 05:32:08.104750'}, {'stderr_lines': [], 'ansible_loop_var': u'item', u'end': u'2020-04-01 05:32:08.761480', 'failed': False, u'stdout': u'', u'changed': True, u'rc': 0, 'item': u'touch /home/target', u'cmd': [u'touch', u'/home/target'], u'stderr': u'', u'delta': u'0:00:00.003149', u'invocation': {u'module_args': {u'creates': None, u'executable': None, u'_uses_shell': False, u'strip_empty_ends': True, u'_raw_params': u'touch /home/target', u'removes': None, u'argv': None, u'warn': True, u'chdir': None, u'stdin_add_newline': True, u'stdin': None}}, 'stdout_lines': [], u'start': u'2020-04-01 05:32:08.758331'}, {'stderr_lines': [u'cp: cannot stat \\u2018/home/lamtv10/lkt\\u2019: No such file or directory'], 'ansible_loop_var': u'item', u'end': u'2020-04-01 05:32:09.222983', u'failed': True, u'stdout': u'', u'changed': True, u'rc': 1, u'start': u'2020-04-01 05:32:09.213547', u'cmd': [u'cp', u'/home/lamtv10/lkt', u'/home/lamtv10/'], 'item': u'cp /home/lamtv10/lkt /home/lamtv10/', u'delta': u'0:00:00.009436', u'invocation': {u'module_args': {u'creates': None, u'executable': None, u'_uses_shell': False, u'strip_empty_ends': True, u'_raw_params': u'cp /home/lamtv10/lkt /home/lamtv10/', u'removes': None, u'argv': None, u'warn': True, u'chdir': None, u'stdin_add_newline': True, u'stdin': None}}, 'stdout_lines': [], u'stderr': u'cp: cannot stat \\u2018/home/lamtv10/lkt\\u2019: No such file or directory', u'msg': u'non-zero return code'}, {'stderr_lines': [], 'ansible_loop_var': u'item', u'end': u'2020-04-01 05:32:09.684698', 'failed': False, u'stdout': u'group_name', u'changed': True, u'rc': 0, 'item': u\"echo 'group_name'\", u'cmd': [u'echo', u'group_name'], u'stderr': u'', u'delta': u'0:00:00.002877', u'invocation': {u'module_args': {u'creates': None, u'executable': None, u'_uses_shell': False, u'strip_empty_ends': True, u'_raw_params': u\"echo 'group_name'\", u'removes': None, u'argv': None, u'warn': True, u'chdir': None, u'stdin_add_newline': True, u'stdin': None}}, 'stdout_lines': [u'group_name'], u'start': u'2020-04-01 05:32:09.681821'}], 'warnings': [u\"Consider using the file module with state=touch rather than running 'touch'.  If you need to use command because file is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in ansible.cfg torid of this message.\"]}"


json_data = log

print( ast.literal_eval(json_data))


print("+++++++++++++++++++=")
loaded_json = json.dumps(ast.literal_eval(json_data))
print(loaded_json)
# #print(task_log)
# print(str(log.encode('utf-8')))
#
# json_log = json.loads(str(log.encode('utf-8')))
# print( json_log)