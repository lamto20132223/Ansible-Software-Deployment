from runnertest import Runner

runner = Runner('/root/app/static/ansible/playbooks/playbook_setup_init_repo_for_controller01.yml',
                '/root/app/static/ansible/inventory/new_node', {'extra_vars': {}, 'tags': ['install', 'uninstall']},
                'debug 2', True, None, None, None)

print(runner.variable_manager)

log_run = runner.run()
print(log_run)