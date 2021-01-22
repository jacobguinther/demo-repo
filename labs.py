from models import config1, config2
from models.experiments import exp

# build from source https://github.com/BlockScience/cadCAD-cs/tree/docker
from cadCAD.configuration.utils import filter_jobs

# Artifact 1
exp.model_ids

# mocking UI input
model_filter = ['sys_model_1', 'sys_model_2', 'sys_model_3']

# Artifact 2: cadCAD.configuration.utils.filter_jobs
client_modules = [config1, config2] # I believe i can auto append module.__name__ with exp.append_model / _config
server_module = 'app.main' # exp is updated with this (via method) which triggers job ser
filtered_jobs, filtered_jobs_lens, renamed_client_modules, exp = filter_jobs(
    experiment=exp,
    client_modules=client_modules,
    server_module=server_module, # exp is updated with this (via method) which triggers job ser
    model_ids=model_filter # mocking UI input
)

def GetModels():
  print(",".join(model_filter))
