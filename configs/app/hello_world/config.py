from utils.config import Config, EvalConfig, TrainConfig


##############################################
#### Application
##############################################

# Hello World Application
cfg = Config(
                name='hello_world',
                services=[
                            'helloworld', 
                        ],
                deployments={
                                'helloworld': 30,
                            },
                cpu_requests=600,
                mem_requests=2000,
                #host='http://104.198.190.0/hello',
                host='http://35.232.59.72/hello',
                autoscale_path='',
                cluster_name='cola-test',
                #cluster_name='istio-stackdriver-demo',
                project_name='vig-cloud',
                zone='us-central1-c',
                #zone='us-central1-f'
           )
