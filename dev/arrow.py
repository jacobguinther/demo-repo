# from pprint import pprint
#
# import pyarrow as pa
# import numpy as np
# import requests
#
# import config1
# from experiments import exp
#
# job = exp.configs[0]
# url = 'http://0.0.0.0:5000'
# endpoint = f'{url}/arrow'
# psubs = job.partial_state_update_blocks
#
# buf = pa.serialize(psubs).to_buffer()
#
# # print(buf.to_pybytes())
#
# # restored_data = pa.deserialize(buf)
# # pprint(restored_data)
#
# r = requests.post(endpoint, data=buf.to_pybytes())
# print(r.text)
# print()
# # print(buf.size)
# #
# #
# # restored_data = pa.deserialize(buf)
# #
# # pprint(restored_data[0])