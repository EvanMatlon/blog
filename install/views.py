import os
import sys
import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect 

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor
# Create your views here.


def index(request):
	return render(request,'index.html')

def install(request):
        if 'ip' in request.GET:
        	ip = request.GET['ip']
                host = []
                host.append(ip)
                #hostdata = {"ansible":{"hosts":host}}
                #host_json = json.dumps(hostdata,indent=4)
                #json.dump(hostdata,open('/etc/ansible/host.txt','w'),indent=4)
                #host_json = {
    	        #		"ansible": {
        	#		"hosts": [
                #				"192.168.164.232", 
        	#			]
    		#		}, 
	        #} 
                              
                         
                variable_manager = VariableManager()
		loader = DataLoader()
                #print  host_json
		inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list=host)
		playbook_path = '/etc/ansible/main.yml'

		if not os.path.exists(playbook_path):
    			print '[INFO] The playbook does not exist'
    			sys.exit()

		Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file','ssh_common_args','ssh_extra_args','sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])
		options = Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=100, remote_user='root', private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method=None, become_user='root', verbosity=None, check=False)

#variable_manager.extra_vars = {'hosts': 'websrvs'} # This can accomodate various other command line arguments.`

		passwords = {}

		pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=passwords)

		results =  pbex.run()

		print results
	        return HttpResponse(results)
                               
        else:
                return HttpResponse("error input")