import codecs
import functools
import operator
import requests


def post_jobs(endpoint: str, filtered_jobs: dict, client_modules, server_module='app.main'):
    renamed_client_modules = []
    for module in client_modules:
        renamed_client_modules.append(module.__name__)

    pkl_jobs = functools.reduce(operator.iconcat, filtered_jobs.values(), [])
    reponses = []
    for pkl_job in pkl_jobs:
        response = requests.post(
            endpoint,
            json={
                'job': pkl_job,  # re_encode(pkl_job),
                'client_modules': renamed_client_modules,
                'server_module': server_module
            }
        )
        reponses.append(response)
        print()
        print(response.text)
    return reponses


# json re_formatter
def re_encode(pkl_obj):
    return codecs.encode(pkl_obj, "base64").decode()