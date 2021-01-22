from cadCAD.configuration import Experiment

from models.config1 import *

exp2 = Experiment()

exp2.append_model(
    user_id='user_a',
    model_id='sys_model_1',
    sim_configs=sim_config,
    initial_state=genesis_states,
    env_processes=env_processes,
    partial_state_update_blocks=partial_state_update_blocks,
    seeds=seeds
)

# exp.append_model(
#     user_id='user_a',
#     model_id='sys_model_2',
#     sim_configs=config2.sim_config,
#     initial_state=config2.genesis_states,
#     env_processes=config2.env_processes,
#     partial_state_update_blocks=config2.partial_state_update_blocks
# )


url = 'http://0.0.0.0:5000'
# endpoint = f'{url}/standard'
#
# job = exp2.get_jobs()[0]
# pkl_job = dill.dumps(job)
# r = requests.post(endpoint, data=pkl_job)
# print(r.text)
# print()

endpoint = f'{url}/psubs'

psubs = [
    {
        "policies": {
            "b1": p1m1,
            "b2": p2m1
        },
        "variables": {
            "s1": s1m1,
            "s2": s2m1,
            "s3": es3,
            "s4": es4,
            "timestamp": update_timestamp
        }
    },
    {
        "policies": {
            "b1": p1m2,
            "b2": p2m2
        },
        "variables": {
            "s1": s1m2,
            "s2": s2m2,
            # "s3": es3p1,
            # "s4": es4p2,
        }
    },
    {
        "policies": {
            "b1": p1m3,
            "b2": p2m3
        },
        "variables": {
            "s1": s1m3,
            "s2": s2m3,
            # "s3": es3p1,
            # "s4": es4p2,
        }
    }
]
s1m1.__module__ = 'app.main'
p1m1.__module__ = 'app.main'
p2m1.__module__ = 'app.main'
s1m1.__module__ = 'app.main'
s2m1.__module__ = 'app.main'
es3.__module__ = 'app.main'
es4.__module__ = 'app.main'
update_timestamp.__module__ = 'app.main'
p1m2.__module__ = 'app.main'
p2m2.__module__ = 'app.main'
s1m2.__module__ = 'app.main'
s2m2.__module__ = 'app.main'
p1m3.__module__ = 'app.main'
p2m3.__module__ = 'app.main'
s1m3.__module__ = 'app.main'
s2m3.__module__ = 'app.main'

pkl_psubs = dill.dumps(psubs)

r = requests.post(endpoint, data=pkl_psubs)
print(r.text)
print()
