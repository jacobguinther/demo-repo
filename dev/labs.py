import codecs
from pprint import pprint

import dill
import requests
from cadCAD.configuration import Configuration
from cadCAD.configuration.utils import filter_jobs
from models import config1
from models.experiments import exp

job = exp.configs[0]
url = 'http://0.0.0.0:5000'
endpoint = f'{url}/struct'
psubs: Configuration = job.partial_state_update_blocks
# dill.settings['recurse'] = True
pkl_str = dill.dumps(config1.psub_struct)
r = requests.post(endpoint, data=pkl_str)
print(r.text)
print()

exit()

pkl_str = dill.dumps(psubs[0])

# output = open('psubs.pkl', 'wb')
# dill.dump(psubs[0], output)
# print(job.__module__)
# exit()

pkl_str = dill.dumps(psubs[0])
# print(pkl_str)
# exit()
# enc_pkl_str = codecs.encode(pkl_str, "base64").decode()
requests.post(endpoint, data=pkl_str)

# pkl_file = open('psubs.pkl', 'rb')
#
# data1 = dill.load(pkl_file)
# pprint(data1)

exit()


decoded_job = codecs.decode(exp.ser_flattened_configs[0].encode(), "base64")
unpickled_job = dill.loads(decoded_job)
# dill.dumps(unpickled_job)
re_encoded_job = codecs.encode(dill.dumps(unpickled_job), "base64").decode()
pprint(unpickled_job)

url = 'http://0.0.0.0:5000'
endpoint = f'{url}/ep'
r = requests.post(endpoint, json={"job": re_encoded_job})
print(r.text)
print()

exit()

model_ids = exp.model_ids

# print(exp.model_job_map)
#
# === Following not in labs.py
# API sends a list of labels to UI
# User selects labels
model_filter = [model_ids[0]]
# print(model_filter)
# selected labels > UI > API > job_writer.py
# ====
filtered_jobs, filtered_jobs_lens = filter_jobs(exp, model_filter)

ser_config = filtered_jobs['sys_model_1'][0]
# job = exp.configs[0]
#
# encoded_psubs = codecs.encode(dill.dumps(exp.configs[0].partial_state_update_blocks), "base64").decode()


# print(ser_config)
# exit()
url = 'http://0.0.0.0:5000'
endpoint = f'{url}/ep'
r = requests.post(endpoint, json={"job": ser_config})
print(r.text)
print()
# print(filtered_jobs_lens)