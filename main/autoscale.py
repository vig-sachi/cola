import os, sys
sys.path.insert(1, os.getcwd())

import utils.cluster as cluster
import utils.launch_apps as launch
import utils.hpa as hpa_utils

# COLA Autoscaling imports.
from training.cola.train_bandit import BanditTrainer
from evaluation.cola.evaluation_cola import FixedRateWorkloadBandit
from inference.cola.inference_cola import BanditAutoscaler

# CPU Autoscaling imports.
from evaluation.cpu_threshold.evaluation_cpu import FixedRateWorkloadCPU


class Autoscaler(object):
    def __init__(self, config, train_config=None, eval_config=None, auth=True):
        self.config = config
        self.train_config = train_config
        self.eval_config = eval_config
        self.auth = auth

        # Create logging directories if they do not exist.
        self.make_dirs()
        self.auth_cluster()

        return

    def create_cluster(self):

        # Authenticate to Google Cloud if requested.
        if self.auth is True:
            cluster.gcloud_authentication()
        
        # Set the project for our Google Cloud CLI.
        cluster.set_project(self.config.project_name)

        # Create the cluster.
        cluster.create_cluster(self.config.project_name, self.config.cluster_name, self.config.zone)

        # Install Istio on cluster.
        cluster.enable_istio_cluster(self.config.project_name, self.config.cluster_name, self.config.zone)

        return

    def auth_cluster(self):
        cluster.authenticate(self.config.cluster_name, self.config.project_name, self.config.zone)
        return

    def launch_application(self):
        launch.launch_application(app_name=self.config.name)
        return

    def train(self, method='cola', run_name='cola'):

        if method == 'cola':
            bt = BanditTrainer(
                                name=run_name,
                                config=self.config, 
                                train_config=self.train_config
                                )
            # Run Training
            #bt.run()

            # Record context we trained on.
            bt.create_context_map()

        return
    
    def evaluate(self, method='cola'):

        # Instantiate class to run evaluation based on the method indicated.
        if method == 'cola':
            frw = FixedRateWorkloadBandit(eval_config=self.eval_config)
        elif method == 'cpu':
            frw = FixedRateWorkloadCPU(self.eval_config)
        
        # Run evaluation.
        frw.run()

        return
    
    def inference(self, method='cola'):

        if method == 'cola':
            ba = BanditAutoscaler(self.eval_config.train_config_path, 
                             self.eval_config.pod_filter, 
                             len(self.eval_config.services))
            ba.run()

        elif method == 'cpu':
            # Runs the first CPU policy defined in the evaluation config.
            hpa_utils.update_autoscaling_policy(config=self.eval_config,
                                                cpu_t=self.eval_config.cpu_policies[0])

        return

    def make_dirs(self):

        for directory in ['logs', 'logs/scratch']:
            path = os.getcwd() + directory

            # Check whether the specified path exists or not
            isExist = os.path.exists(path)

            if not isExist:
                # Create a new directory because it does not exist 
                os.makedirs(path)

        return
