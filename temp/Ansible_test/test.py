import ansible_runner

#runner = ansible.runner.Runner(
 #  module_name='ping',
#   module_args='',
 #  pattern='localhost'
#)
#datastructure = runner.run()
print("执行module")
m = ansible_runner.run(host_pattern='localhost', module='ping',module_args='')