import pandas as pd
from tabulate import tabulate

from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from models.experiments import exp

exec_mode = ExecutionMode()
local_proc_ctx = ExecutionContext(context=exec_mode.local_mode)
run = Executor(exec_context=local_proc_ctx, configs=exp.configs, empty_return=False)  # Option: Disable mem w/

raw_result, tensor_fields, sessions = run.execute()
result = pd.DataFrame(raw_result)
# pprint(sessions)
print(tabulate(result, headers='keys', tablefmt='psql'))