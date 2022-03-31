import os, sys
sys.path.insert(1, os.getcwd())

import utils.cluster as cluster
import utils.launch_apps as launch
from training.cola.train_bandit import BanditTrainer

class COLA(object):
    def __init__(self, config, train_config=None, eval_config=None, auth=True):
        self.config = config
        self.train_config = train_config
        self.eval_config = eval_config
        self.auth = auth
        return

    def create_cluster(self):

        # Authenticate to Google Cloud if requested.
        if self.auth is True:
            cluster.gcloud_authentication()
        
        # Set the project for our Google Cloud CLI.
        cluster.set_project(self.config.project_name)

        # Create the cluster.
        cluster.create_cluster(self.config.project_name, self.config.cluster_name, self.config.zone)

        return

    def auth_cluster(self):
        cluster.authenticate(self.config.cluster_name, self.config.project_name, self.config.zone)
        return

    def launch_application(self):
        launch.launch_application(app_name=self.config.name)
        return

    def train_autoscaler(self, method='cola', run_name='cola'):

        if method == 'cola':
            # Run Training
            bt = BanditTrainer(
                                name=run_name,
                                config=self.config, 
                                train_config=self.train_config
                                )
            bt.run()
        return
    
    def evaluate_autoscaler(self):
        return
    
    def inference_autoscaler(self):
        return
