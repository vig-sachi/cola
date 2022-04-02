import os
import sys
import json
import time

sys.path.insert(1, '/home/packard2700/autoscale-bandit')
from utils.kube_utils import get_current_deployments

# File name, remove the old log on start
fname = 'service_replicas_count.json'
wait_time = 10 # Interval at which we get results


def run():
    
    # Remove log file if it exists.
    os.system('rm {}'.format(fname))

    while True:
        try:
            deployments = get_current_deployments()
            res_dict = {   
                        'deployments': deployments,
                        'services': list(deployments.keys()), 
                        'tot_replicas': sum(deployments.values()), 
                        'time': time.time(),
                        }
            with open(fname, 'a+') as obj:
                obj.write(json.dumps(res_dict) + '\n')
            time.sleep(wait_time)

        except:
            pass


if __name__ == "__main__":
    run()