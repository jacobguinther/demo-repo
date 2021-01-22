import codecs
import pickle
import sys
from copy import deepcopy

import dill
import requests

from models import config1
from models.experiments import exp

# print(exp.ser_flattened_configs)
# exit()
jobs = deepcopy(exp.configs)

url = 'http://0.0.0.0:5000'
# print(type(jobs[0]))
# exit()
dill.detect.trace(True)

print()
job = jobs[0]
job_dict = job.__dict__

# print(job.__name__)
# print(job.__module__)
# exit()

sys.modules['config1'] = config1

r = requests.post(f'{url}/psubs', json={
        # "psub": codecs.encode(cloudpickle.dumps(job.partial_state_update_blocks[0]), "base64").decode(),
        "partial_state_update_blocks": codecs.encode(dill.dumps(job.partial_state_update_blocks), "base64").decode(),
        # "config1": codecs.encode(dill.dumps(config1), "base64").decode()
    }
)

# r = requests.post(f'{url}/psubs', json={
#         "config1": codecs.encode(dill.dumps(config1), "base64").decode()
#     }
# )

# r = requests.post(f'{url}/psubs', json={
#         "partial_state_update_blocks": codecs.encode(hickle.dumps(job.partial_state_update_blocks), "base64").decode()
#     }
# )

print(r.text)
print()

exit()


# print(job_dict)
# c = Configuration(
#     user_id=job.user_id, model_id=job.model_id, subset_id=job.subset_id,
#     subset_window=job.subset_window, sim_config=job.sim_config, initial_state=job.initial_state,
#     seeds=job.seeds, env_processes=job.env_processes, exogenous_states=job.exogenous_states,
#     partial_state_update_blocks=job_dict['partial_state_update_blocks']
# )
r = requests.post(f'{url}/test', json={
        "user_id": codecs.encode(pickle.dumps(job.user_id), "base64").decode(),
        "model_id": codecs.encode(pickle.dumps(job.model_id), "base64").decode(),
        "subset_id": codecs.encode(pickle.dumps(job.subset_id), "base64").decode(),
        "subset_window": codecs.encode(pickle.dumps(job.subset_window), "base64").decode(),
        "sim_config": codecs.encode(pickle.dumps(job.sim_config), "base64").decode(),
        "initial_state": codecs.encode(pickle.dumps(job.initial_state), "base64").decode(),
        "seeds": codecs.encode(pickle.dumps(job.seeds), "base64").decode(),
        # "env_processes": codecs.encode(dill.dumps(job.env_processes), "base64").decode(),
        "exogenous_states": codecs.encode(pickle.dumps(job.exogenous_states), "base64").decode(),
        # "partial_state_update_blocks": codecs.encode(dill.dumps(job.partial_state_update_blocks), "base64").decode()
    }
)
# c.__dict__ = jobs.__dict__
# print(c)
# exit()

# r = requests.post(f'{url}/test', data={"test": codecs.encode(dill.dumps(jobs[0]), "base64").decode()})

# r = requests.post(f'{url}/test', data={"test": codecs.encode(dill.dumps(1), "base64").decode()})
# r = requests.post(f'{url}/test', data={"test": dill.dumps(jobs[0])})
print(r.text)
print()

exit()

url = 'http://0.0.0.0:5000'
# url = 'http://192.168.49.2:30483'
# url = 'http://a17d94fc39ce44bf98329abd09edcd42-1800703071.us-east-2.elb.amazonaws.com'
jobs = deepcopy(exp.ser_flattened_configs)
# print(type(jobs))
# exit()
send_list = [f'{url}/execute'] * len(jobs)
send_map = dict(zip(jobs, send_list))
# pprint(send_map)

map_list = list(send_map.items())

new_send_map = dict([map_list[0], map_list[3]])
single_run_map = dict([map_list[0]])

# for x in exp.configs:
#     print()
#     pprint(x.__dict__)
# exit()



# for ser_config, endpoint in single_run_map.items():
#     r = requests.post(endpoint, data={"job": ser_config})
#     print(r.text)
#     print()
# pprint(new_send_map)

# print(map_list[0])
# print()
# exp.send(send_list)
# exp.send(new_send_map)
# exp.send(single_run_map)

# exp.send(send_map)
# pprint(send_map)

# Run
