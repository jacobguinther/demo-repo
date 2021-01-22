import codecs
from copy import deepcopy

import dill
import requests
from cadCAD.configuration import Configuration

from models import config1
# from config1 import job
from models.experiments import exp

dill.detect.trace(True)
url = 'http://0.0.0.0:5000'

dc_psub = deepcopy(config1.partial_state_update_blocks)
new_config1 = config1
new_psubs = [{deepcopy(k): deepcopy(v) for k, v in deepcopy(psub).items()} for psub in deepcopy(new_config1.partial_state_update_blocks)]
pickled_encoded_psubs = codecs.encode(dill.dumps(new_psubs), "base64").decode()
pickled_encoded_job = codecs.encode(dill.dumps(new_psubs[0]), "base64").decode()

# r = requests.post(f'{url}/psubs', data=pickled_encoded_psubs)
r = requests.post(f'{url}/psubs', json={'job': pickled_encoded_job})
print(r.text)
print()
exit()

# r = requests.post(f'{url}/psubs', json={'partial_state_update_blocks': pickled_encoded_psub})
# print(r.text)
# print()
# exit()

job = deepcopy(exp.configs[0])

local_job = Configuration(
    user_id=job.user_id, model_id=job.model_id, subset_id=job.subset_id,
    subset_window=job.subset_window, sim_config=job.sim_config, initial_state=job.initial_state,
    seeds=job.seeds, env_processes=job.env_processes, exogenous_states=deepcopy(job.exogenous_states),
    partial_state_update_blocks=deepcopy(job.partial_state_update_blocks)
)
pickled_encoded_job = codecs.encode(dill.dumps(local_job), "base64").decode()
# print(c)
r = requests.post(f'{url}/job', json={'job': pickled_encoded_job})
print(r.text)
print()
exit()

# r = requests.post(f'{url}/job', json={'job': config1.ser_job})
# print(r.text)
# print()

# job = exp.configs[0]
# pickled_encoded_job = codecs.encode(dill.dumps(job), "base64").decode()

# job = exp.ser_flattened_configs[0]
# pickled_encoded_job = codecs.encode(job, "base64").decode()
# r = requests.post(f'{url}/job', json={'job': pickled_encoded_job})
# print(r.text)
# print()

r = requests.post(f'{url}/psubs', json={
        "partial_state_update_blocks": config1.encoded_psubs
        # "partial_state_update_blocks": pickled_encoded_job
    }
)

print(r.text)
print()

