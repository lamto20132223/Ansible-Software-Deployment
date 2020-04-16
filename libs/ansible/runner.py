#https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_filter_operators.htm
#https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html
# https://docs.ansible.com/ansible/latest/user_guide/playbooks_startnstep.html
# https://docs.ansible.com/ansible/latest/user_guide/playbooks_tags.html
# https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python


import os
import sys
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor import playbook_executor


from tempfile import NamedTemporaryFile
from ansible.utils.display import Display


import global_assets.const as CONST



class Options(object):
    """
    Options class to replace Ansible OptParser
    """
    def __init__(self, verbosity=None, inventory=None, listhosts=False, subset=None, module_paths=None, extra_vars=None,
                 forks=100, ask_vault_pass=None, vault_password_files=None, new_vault_password_file=None,
                 output_file=None, tags=None, skip_tags=None, one_line=None, tree=None, ask_sudo_pass=None, ask_su_pass=None,
                 sudo=None, sudo_user=None, become=True, become_method='sudo', become_user='root', become_ask_pass=None,
                 ask_pass=None, private_key_file=None, remote_user='root', connection='ssh', timeout=None, ssh_common_args=None,
                 sftp_extra_args=None, scp_extra_args=None, ssh_extra_args=None, poll_interval=None, seconds=None, check=False,
                 syntax=False, diff=False, force_handlers=None, flush_cache=None, listtasks=False, listtags=False, module_path=None, start_at_task=None, step=None):
        self.verbosity = verbosity
        self.inventory = inventory
        self.listhosts = listhosts
        self.subset = subset
        self.module_paths = module_paths
        self.extra_vars = extra_vars
        self.forks = forks
        self.ask_vault_pass = ask_vault_pass
        self.vault_password_files = vault_password_files
        self.new_vault_password_file = new_vault_password_file
        self.output_file = output_file
        self.tags = tags
        self.skip_tags = skip_tags
        self.one_line = one_line
        self.tree = tree
        self.ask_sudo_pass = ask_sudo_pass
        self.ask_su_pass = ask_su_pass
        self.sudo = sudo
        self.sudo_user = sudo_user
        self.become = become
        self.become_method = become_method
        self.become_user = become_user
        self.become_ask_pass = become_ask_pass
        self.ask_pass = ask_pass
        self.private_key_file = private_key_file
        self.remote_user = remote_user
        self.connection = connection
        self.timeout = timeout
        self.ssh_common_args = ssh_common_args
        self.sftp_extra_args = sftp_extra_args
        self.scp_extra_args = scp_extra_args
        self.ssh_extra_args = ssh_extra_args
        self.poll_interval = poll_interval
        self.seconds = seconds
        self.check = check
        self.syntax = syntax
        self.diff = diff
        self.force_handlers = force_handlers
        self.flush_cache = flush_cache
        self.listtasks = listtasks
        self.listtags = listtags
        self.module_path = module_path
        self.start_at_task= start_at_task
        self.step = step

    def get_config(self):

        Configs = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check','diff','start_at_task','step','tags'])
        return Configs(listtags=self.listtags, listtasks=self.listtasks, listhosts=self.listhosts, syntax=self.syntax, connection=self.connection, module_path=self.module_path, forks=self.forks, remote_user=self.remote_user, private_key_file=self.private_key_file, ssh_common_args=self.ssh_common_args, ssh_extra_args=self.ssh_extra_args, sftp_extra_args=self.sftp_extra_args, scp_extra_args=self.scp_extra_args, become=self.become, become_method=self.become_method , become_user=self.become_user, verbosity=self.verbosity, check=self.check, diff=self.diff, start_at_task=self.start_at_task, step=self.step, tags=self.tags)



class Runner(object):

    def __init__(self, playbook,inventory,run_data, start_at_task, step,private_key_file , become_pass, verbosity=0 ):

        self.run_data = run_data

        self.options = Options()
        self.options.listtags=False
        self.options.listtasks=False
        self.options.listhosts=False
        self.options.syntax=False
        self.options.check=False
        self.options.diff=False
        self.options.start_at_task = start_at_task
        self.options.step = step


        self.options.private_key_file = private_key_file
        self.options.verbosity = verbosity
        self.options.connection = 'ssh'  # Need a connection type "smart" or "ssh"
        self.options.become = False
        self.options.become_method = 'sudo'
        self.options.become_user = 'root'
        self.options.remote_user = 'root'
        # Set global verbosity
        self.display = Display()
        self.display.verbosity = self.options.verbosity

        self.log = {"processed":"0", "failures":"0", "ok":"0","dark":"0","changed":"0","skipped":"0", 'summarize':{}}

        # Executor appears to have it's own
        # verbosity object/setting as well
        #playbook_executor.verbosity = self.options.verbosity

        # Become Pass Needed if not logging in as user root
        passwords = {'become_pass': become_pass}

        # Gets data from YAML/JSON files
        self.loader = DataLoader()
       # self.loader.set_vault_password(os.environ['VAULT_PASS'])

        # All the variables from all the various places


        # Parse hosts, I haven't found a good way to
        # pass hosts in without using a parsed template :(
        # (Maybe you know how?)
#         self.hosts = NamedTemporaryFile(delete=False)
#         self.hosts.write("""[run_hosts]
# %s
# """ % hostnames)
#         self.hosts.close()

        # This was my attempt to pass in hosts directly.
        #
        # Also Note: In py2.7, "isinstance(foo, str)" is valid for
        #            latin chars only. Luckily, hostnames are
        #            ascii-only, which overlaps latin charset
        ## if isinstance(hostnames, str):
        ##     hostnames = {"customers": {"hosts": [hostnames]}}

        # Set inventory, using most of above objects
        inventory_dir= CONST.inventory_dir
        inventory_source = "%s/%s" % (inventory_dir, inventory)
        self.inventory = InventoryManager(loader=self.loader, sources=inventory_source)
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
        if self.run_data:
            self.variable_manager.extra_vars = self.run_data['extra_vars']
            self.options.tags = self.run_data['tags']

        # Playbook to run. Assumes it is
        # local to this python file
        pb_dir = CONST.playbook_dir
        playbook = "%s/%s" % (pb_dir, playbook)
        print(playbook)
        # Setup playbook executor, but don't run until run() called
        self.pbex = playbook_executor.PlaybookExecutor
        self.pbex = playbook_executor.PlaybookExecutor(
            playbooks=[playbook],
            inventory=self.inventory,
            variable_manager=self.variable_manager,
            loader=self.loader,
            options=self.options.get_config(),
            passwords=passwords)

    def run(self):
        # Results of PlaybookExecutor
        cb =self.pbex._tqm._stdout_callback
        self.pbex.run()
        stats = self.pbex._tqm._stats
        print(stats)



        # Test if success for record_logs
        run_success = True
        hosts = sorted(stats.processed.keys())

        for index,h in  enumerate(hosts,start=1):
            t = stats.summarize(h)
            self.log["summarize"][index]=[h,t]
            if t['unreachable'] > 0 or t['failures'] > 0:
                run_success = False



        # Dirty hack to send callback to save logs with data we want
        # Note that function "record_logs" is one I created and put into
        # the playbook callback file
        self.pbex._tqm.send_callback(
            'record_logs',
            success=run_success
        )

        self.log['processed'] = stats.processed
        self.log['failures'] = stats.failures
        self.log['ok'] = stats.ok
        self.log['dark'] = stats.dark
        self.log['changed'] = stats.changed
        self.log['skipped'] = stats.skipped
        self.log['cb'] = cb

        return stats

    def terminate(self):
        self.pbex._tqm.terminate()



def print_stats(stats):
#https://fossies.org/linux/ansible/lib/ansible/executor/stats.py
    print("processed: ")
    print(stats.processed)
    print("failures: ")
    print(stats.failures)
    print("ok: ")
    print(stats.ok)
    print("dark: ")
    print(stats.dark)
    print("changed: ")
    print(stats.changed)
    print("skipped: ")
    print(stats.skipped)
    # print("rescued: ")
    # print(stats.rescued)
    # print("ignored: ")
    # print(stats.ignored)

def get_stats(stats):
#https://fossies.org/linux/ansible/lib/ansible/executor/stats.py
    return {"processed: " : str(stats.processed),
            "failures: " : str(stats.failures),
            "ok: " : str(stats.ok),
            "dark: ": str(stats.dark),
            "changed: ": str(stats.changed),
            "skipped: ": str(stats.skipped)
            }

class Checker(object):

    def __init__(self, playbook,inventory,run_data, start_at_task, step,private_key_file , become_pass, verbosity=0 ):

        self.run_data = run_data

        self.options = Options()
        self.options.listtags=False
        self.options.listtasks=False
        self.options.listhosts=False
        self.options.syntax=False
        self.options.check=True
        self.options.diff=False
        self.options.start_at_task = start_at_task
        self.options.step = step


        self.options.private_key_file = private_key_file
        self.options.verbosity = verbosity
        self.options.connection = 'ssh'  # Need a connection type "smart" or "ssh"
        self.options.become = False
        self.options.become_method = 'sudo'
        self.options.become_user = 'root'
        self.options.remote_user = 'root'
        # Set global verbosity
        self.display = Display()
        self.display.verbosity = self.options.verbosity
        # Executor appears to have it's own
        # verbosity object/setting as well
        #playbook_executor.verbosity = self.options.verbosity

        # Become Pass Needed if not logging in as user root
        passwords = {'become_pass': become_pass}

        # Gets data from YAML/JSON files
        self.loader = DataLoader()
       # self.loader.set_vault_password(os.environ['VAULT_PASS'])

        # All the variables from all the various places


        # Parse hosts, I haven't found a good way to
        # pass hosts in without using a parsed template :(
        # (Maybe you know how?)
#         self.hosts = NamedTemporaryFile(delete=False)
#         self.hosts.write("""[run_hosts]
# %s
# """ % hostnames)
#         self.hosts.close()

        # This was my attempt to pass in hosts directly.
        #
        # Also Note: In py2.7, "isinstance(foo, str)" is valid for
        #            latin chars only. Luckily, hostnames are
        #            ascii-only, which overlaps latin charset
        ## if isinstance(hostnames, str):
        ##     hostnames = {"customers": {"hosts": [hostnames]}}

        # Set inventory, using most of above objects
        inventory_dir= CONST.inventory_dir
        inventory_source = "%s/%s" % (inventory_dir, inventory)
        self.inventory = InventoryManager(loader=self.loader, sources=inventory_source)
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
        if self.run_data:
            self.variable_manager.extra_vars = self.run_data['extra_vars']
            self.options.tags = self.run_data['tags']

        # Playbook to run. Assumes it is
        # local to this python file
        pb_dir = CONST.playbook_dir
        playbook = "%s/%s" % (pb_dir, playbook)
        print(playbook)
        # Setup playbook executor, but don't run until run() called
        self.pbex = playbook_executor.PlaybookExecutor
        self.pbex = playbook_executor.PlaybookExecutor(
            playbooks=[playbook],
            inventory=self.inventory,
            variable_manager=self.variable_manager,
            loader=self.loader,
            options=self.options.get_config(),
            passwords=passwords)

    def run(self):
        # Results of PlaybookExecutor
        self.pbex.run()
        stats = self.pbex._tqm._stats
        print(stats)

        # Test if success for record_logs
        run_success = True
        hosts = sorted(stats.processed.keys())
        for h in hosts:
            t = stats.summarize(h)
            if t['unreachable'] > 0 or t['failures'] > 0:
                run_success = False

        # Dirty hack to send callback to save logs with data we want
        # Note that function "record_logs" is one I created and put into
        # the playbook callback file
        self.pbex._tqm.send_callback(
            'record_logs',
            success=run_success
        )



        return stats




if __name__=="__main__":
    #test_add_nodes()
    print("lamtv10")
    runner = Runner('ansible_compute.yml','multnode',{'extra_vars':{'target':"lamtv10"} ,'tags':['install','uninstall']},None, False,  None,None,None)
    stats = runner.run()
    print_stats(stats)


    runner2 = Runner('ansible_compute.yml','multnode',{'extra_vars':{'target':"ta2"} ,'tags':['install','uninstall']},None, False,  None,None,None)
    stats2 = runner2.run()
    print_stats(stats2)


