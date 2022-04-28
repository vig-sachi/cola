from utils.config import Config, EvalConfig, TrainConfig

##############################################
#### Application Config
##############################################

# Book Info Application
cfg = Config(
                name='book_info',
                services=[
                            'details', 
                            'productpage', 
                            'ratings', 
                            'reviews', 
                        ],
                deployments={
                                'details': 20,
                                'productpage': 40, 
                                'ratings': 20,
                                'reviews': 20,
                            },
                cpu_requests=600,
                mem_requests=2000,
                host='',
                autoscale_path='',
                cluster_name='cola-test',
                project_name='vig-cloud',
                zone='us-central1-c',
            )