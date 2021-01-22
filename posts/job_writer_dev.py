from models import config1, config2
from models.experiments import exp

from cadCAD.configuration.utils import filter_jobs

from utils import post_jobs

# url = 'http://0.0.0.0:5000'
# url = 'http://0.0.0.0:5001'
url = 'http://192.168.49.2:30231'
# url = 'http://aee82f162b0e14391a1fa0648e6a05d1-1274469206.us-east-2.elb.amazonaws.com'
endpoint = f'{url}/execute'

# dill.detect.trace(True)
# ** get module name from append_model

# exp.model_ids
model_filter = ['sys_model_1', 'sys_model_2'] # mocking UI input
client_modules = [config1, config2]
# model_filter = ['sys_model_1'] # mocking UI input
# client_modules = [config1]
server_module = 'main' # exp is updated with this (via method) which triggers job ser
filtered_jobs, filtered_jobs_lens, renamed_client_modules, exp = filter_jobs(
    experiment=exp,
    client_modules=client_modules,
    server_module=server_module, # exp is updated with this (via method) which triggers job ser
    model_ids=model_filter # mocking UI input
)
# pkl_job = filtered_jobs[model_filter[0]][0] # sys_model_1

post_jobs(endpoint, filtered_jobs, client_modules, server_module)


# r_job = requests.post(
#     endpoint,
#     json={
#         'job': pkl_job, #re_encode(pkl_job),
#         'client_modules': renamed_client_modules,
#         'server_module': server_module
#     }
# )
#
# print(r_job.text)
# print()

# json.dumps(dict)
# dill.dumps(dict)
