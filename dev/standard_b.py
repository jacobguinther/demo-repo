# import codecs

import dill
import requests
# from cadCAD.configuration import Configuration

from models import config1
from utils import re_assign_modules, re_encode
from models.experiments import exp


url = 'http://0.0.0.0:5000'
endpoint = f'{url}/execute'

dill.detect.trace(True)
server_module = 'app.main' # exp is updated with this (via method) which triggers job ser
# psubs = re_assign_modules['psubs'](config1.partial_state_update_blocks, server_module)
configs = re_assign_modules(exp.configs, server_module)

# * bug: pickling - link previous JIRA issue
# * New Feature for cadCAD K8s Service addressing bug (potentially Pythons pickle pkg)

# Next Steps:
# A: exp is updated with server_module (via method) which triggers job ser
# B: re_assign_modules in exp before serialization [exp.ser_flattened_configs (jobs)]
# C: re_assign_modules(exp.configs): exp.configs - of all jobs given exp.configs
# D: re_assign_modules[EVERYTHING]
# Alt:
# * Create Configuration member to hold local vars
# * rename their modules [re_assign_modules(exp.configs)]
# * cadCAD/engine/simulation.py - generate_record:
# ** mod _input OR add additional_objs to include client vars (_input[var] OR additional_objs[var])

job = configs[0]

pkl_job = dill.dumps(job)
modules = [config1.__name__]
r_job = requests.post(
    endpoint,
    json={
        'job': re_encode(pkl_job),
        'client_modules': modules,
        'server_module': server_module
    }
)
print(r_job.text)
print()


