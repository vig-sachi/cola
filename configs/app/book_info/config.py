from utils.config import Config, EvalConfig, TrainConfig

##############################################
#### Application Config
##############################################

# Book Info Application
cfg = Config(
                name='bookinfo',
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
                host='http://35.232.246.231/productpage',
                autoscale_path=''
            )