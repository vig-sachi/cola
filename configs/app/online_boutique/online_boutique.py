from utils.config import Config, EvalConfig, TrainConfig
from microservices.launch_apps import launch_application

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
                host='http://35.232.246.231:80',
                autoscale_path=''
            )

##############################################
#### Training
##############################################

# 1. 50ms Median Latency
train_cfg = TrainConfig(
                            train_rps=[100, 200, 300, 400], 
                            train_iters=10, 
                            latency_threshold=50, 
                            c=2, 
                            w_l=5, 
                            w_i=15, 
                            min_iters=5, 
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=45,
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=130,
                            lat_opt='Average Latency'
                        )

train_cfg_ldr = TrainConfig(
                            train_rps=[50, 200, 500, 800, 1100, 1400, 1700, 2000, 2300, 2600, 2900, 3000],
                            train_iters=15,
                            latency_threshold=100,
                            c=2,
                            w_l=5,
                            w_i=15,
                            min_iters=5,
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=60,
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=130,
                            lat_opt='Average Latency'
                        )


train_cfg2 = TrainConfig(
                            #train_rps=[800], 
                            #train_rps=[200, 400, 600, 800],
                            train_rps=[400, 600],
                            train_iters=15, 
                            latency_threshold=50, 
                            c=2, 
                            w_l=1, 
                            w_i=3, 
                            min_iters=5, 
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=60,
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=100,
                            lat_opt='Average Latency'
                        )



train_cfg_new_target = TrainConfig(
                            train_rps=[200, 400, 600, 800],
                            train_iters=15,
                            latency_threshold=45,
                            c=2,
                            w_l=5,
                            w_i=15,
                            min_iters=5,
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=60,
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=150,
                            lat_opt='Average Latency'
                        )


train_cfgd2 = TrainConfig(
                            train_rps=[200, 400, 600, 800], 
                            train_iters=15, 
                            latency_threshold=50, 
                            c=2, 
                            w_l=5, 
                            w_i=15, 
                            min_iters=5, 
                            locustfile='load_generator/locustfiles/online-boutique/high_purchase.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=60,
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=150,
                            lat_opt='Average Latency'
                        )

train_cfgd3 = TrainConfig(
                            train_rps=[200, 400, 600, 800],
                            train_iters=15,
                            latency_threshold=50,
                            c=2,
                            w_l=5,
                            w_i=15,
                            min_iters=5,
                            locustfile='load_generator/locustfiles/online-boutique/medium_purchase.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=60,
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=150,
                            lat_opt='Average Latency'
                        )


train_cfg3 = TrainConfig(
                            train_rps=[200, 400, 600, 800], 
                            train_iters=15, 
                            latency_threshold=100, 
                            c=2, 
                            w_l=5, 
                            w_i=15, 
                            min_iters=5, 
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=45,
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=60,
                            lat_opt='90p Latency'
                        )



train_cfg_new_tail = TrainConfig(
                            train_rps=[200, 400, 600, 800],
                            train_iters=15,
                            latency_threshold=90,
                            c=2,
                            w_l=5,
                            w_i=15,
                            min_iters=5,
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=45,
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=60,
                            lat_opt='90p Latency'
                        )


train_cfg_cheap1 = TrainConfig(
                            train_rps=[200, 400], 
                            train_iters=15, 
                            latency_threshold=50, 
                            c=2, 
                            w_l=5, 
                            w_i=5, 
                            min_iters=5, 
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=45,
                            cluster_name='online-boutique',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=60,
                            lat_opt='Average Latency',
                        )

train_cfg_cheap2 = TrainConfig(
                            train_rps=[200, 400], 
                            train_iters=15, 
                            latency_threshold=50, 
                            c=2, 
                            w_l=5, 
                            w_i=10, 
                            min_iters=5, 
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=45,
                            cluster_name='online-boutique',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=60,
                            lat_opt='Average Latency',
                        )

train_cfg_cheap4 = TrainConfig(
                            train_rps=[200, 400], 
                            train_iters=15, 
                            latency_threshold=50, 
                            c=2, 
                            w_l=5, 
                            w_i=20, 
                            min_iters=5, 
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=45,
                            cluster_name='online-boutique',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=60,
                            lat_opt='Average Latency',
                        )


train_cfg_cheap5 = TrainConfig(
                            train_rps=[200, 400], 
                            train_iters=15, 
                            latency_threshold=50, 
                            c=2, 
                            w_l=5, 
                            w_i=40, 
                            min_iters=5, 
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            pod_filter='frontend',
                            req_names=[],
                            search_strategy='cpu',
                            sample_duration=45,
                            cluster_name='online-boutique',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            max_nodes=60,
                            lat_opt='Average Latency',
                        )

##############################################
#### Workloads
##############################################

# 1. Fixed Rate Workload (In Sample)
eval_cfg_cpu_fr = EvalConfig(
                            name='fixed_rate_insample2',
                            services=cfg.services, 
                            deployments=cfg.deployments,
                            cpu_requests=600,
                            mem_requests=2000,

                            host='http://34.71.119.136:80',
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            cluster_name='online-boutique',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            min_nodes=1,
                            max_nodes=130,

                            application='online_boutique',
                            rps_rates=[600, 800],
                            cpu_policies=[10,30,50,70,90],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/online_boutique/bandit-50',
                            pod_filter='frontend',
                            duration=60,
                            num_iters=10,
                            wait_time=120,
                            reset_cluster=False
                        )

eval_cfg_cpu_fr_lg = EvalConfig(
                            name='fixed_rate_insample2',
                            services=cfg.services, 
                            deployments=cfg.deployments,
                            cpu_requests=600,
                            mem_requests=2000,

                            host='http://34.71.119.136:80',
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            cluster_name='online-boutique',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            min_nodes=1,
                            max_nodes=130,

                            application='online_boutique',
                            rps_rates=[600, 800],
                            cpu_policies=[10,30,50,70,90],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/online_boutique/bandit-50-large-2',
                            pod_filter='frontend',
                            duration=60,
                            num_iters=10,
                            wait_time=120,
                            reset_cluster=False
                        )


eval_cfg_cpu_fr_med_purchase = EvalConfig(
                            name='fixed_rate_medpurchase',
                            services=cfg.services,
                            deployments=cfg.deployments,
                            cpu_requests=600,
                            mem_requests=2000,

                            host='http://35.232.246.231:80',
                            locustfile='load_generator/locustfiles/online-boutique/medium_purchase.py',
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            min_nodes=1,
                            max_nodes=130,

                            application='online_boutique',
                            rps_rates=[300],
                            cpu_policies=[30,70],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/online_boutique/bandit-50-large',
                            second_context='/home/packard2700/autoscale-bandit/models/online_boutique/bandit-50-high-purchase',
                            pod_filter='frontend',
                            duration=60,
                            num_iters=10,
                            wait_time=120,
                            reset_cluster=False
                        )


eval_cfg_cpu_fr_tail = EvalConfig(
                            name='fixed_rate_insample_tail',
                            services=cfg.services, 
                            deployments=cfg.deployments,
                            cpu_requests=600,
                            mem_requests=2000,

                            host='http://34.71.119.136:80',
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            cluster_name='online-boutique',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            min_nodes=1,
                            max_nodes=130,

                            application='online_boutique',
                            rps_rates=[600, 800],
                            cpu_policies=[10,30,50,70,90],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/online_boutique/bandit-50-tail',
                            pod_filter='frontend',
                            duration=60,
                            num_iters=10,
                            wait_time=120,
                            reset_cluster=False
                        )


eval_cfg_cpu_fr_oos = EvalConfig(
                            name='fixed_rate_oosample',
                            services=cfg.services, 
                            deployments=cfg.deployments,
                            cpu_requests=600,
                            mem_requests=2000,

                            host='http://34.71.119.136:80',
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            cluster_name='online-boutique',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            min_nodes=1,
                            max_nodes=130,

                            application='online_boutique',
                            rps_rates=[150,350],
                            cpu_policies=[10,30,50,70,90],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/online_boutique/bandit-50',
                            pod_filter='frontend',
                            duration=60,
                            num_iters=10,
                            wait_time=120,
                            reset_cluster=False
                        )

# 2. Ramp Workload (In Sample)
eval_cfg_ramp = EvalConfig(
                            name='ramp_insample',
                            services=cfg.services, 
                            deployments=cfg.deployments,
                            cpu_requests=600,
                            mem_requests=2000,

                            host='http://34.71.119.136:80',
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            cluster_name='online-boutique',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            min_nodes=1,
                            max_nodes=130,

                            application='online_boutique',
                            rps_rates=[100,300,400,300,100],
                            cpu_policies=[10,30,50,70,90],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/online_boutique/bandit-50',
                            pod_filter='frontend',
                            duration=600,
                            num_iters=1,
                            wait_time=0,
                            reset_cluster=False
                        )

eval_cfg_ramp_oos = EvalConfig(
                            name='ramp_oosample',
                            services=cfg.services, 
                            deployments=cfg.deployments,
                            cpu_requests=600,
                            mem_requests=2000,

                            host='http://34.71.119.136:80',
                            locustfile='load_generator/locustfiles/online-boutique/default.py',
                            cluster_name='online-boutique',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            min_nodes=1,
                            max_nodes=130,

                            application='online_boutique',
                            rps_rates=[150,250,350,250,150],
                            cpu_policies=[10,30,50,70,90],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/online_boutique/bandit-50',
                            pod_filter='frontend',
                            duration=600,
                            num_iters=1,
                            wait_time=0,
                            reset_cluster=False
                        )
