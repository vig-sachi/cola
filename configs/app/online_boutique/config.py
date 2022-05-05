from utils.config import Config

##############################################
#### Application
##############################################

# Online Boutique Application
cfg = Config(
                name='online_boutique',
                services=[
                            'frontend', 
                            'productcatalogservice', 
                            'currencyservice', 
                            'recommendationservice', 
                            'cartservice', 
                            'adservice', 
                            'checkoutservice', 
                            'shippingservice', 
                            'redis', 
                            'paymentservice', 
                            'emailservice'
                        ],
                deployments={
                                'frontend':30, 
                                'productcatalogservice':10, 
                                'currencyservice':10, 
                                'recommendationservice':10, 
                                'cartservice':10, 
                                'adservice':10, 
                                'checkoutservice':10, 
                                'shippingservice':10, 
                                'redis':10, 
                                'paymentservice':10, 
                                'emailservice':10
                            },
                cpu_requests=600,
                mem_requests=2000,
                host='',
                autoscale_path='',
                cluster_name='cola-test',
                project_name='vig-cloud',
                zone='us-central1-c',
            )

