from utils.config import EvalConfig
from configs.app.book_info.config import cfg

##############################################
#### Evaluations
##############################################

# 1. Fixed Rate Workload (In Sample)
eval_cfg = EvalConfig(
                            name='fixed_rate_insample_colocate',
                            services=cfg.services, 
                            deployments=cfg.deployments,
                            cpu_requests=600,
                            mem_requests=2000,

                            host='',
                            locustfile='microservices/book_info/workloads/default.py',
                            cluster_name='cola-test',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='app-pool',
                            min_nodes=1,
                            max_nodes=96,

                            application='book_info',
                            rps_rates=[800], 
                            cpu_policies=[30,50,70],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/bookinfo/bandit-50',
                            pod_filter='productpage',
                            duration=60,
                            num_iters=25,
                            wait_time=120,
                            reset_cluster=False
                        )



eval_cfg_two_min = EvalConfig(
                            name='fixed_rate_insample_colocate_twomin',
                            services=cfg.services,
                            deployments=cfg.deployments,
                            cpu_requests=600,
                            mem_requests=2000,

                            host='',
                            locustfile='microservices/book_info/workloads/default.py',
                            cluster_name='cola-test',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='app-pool',
                            min_nodes=1,
                            max_nodes=60,

                            application='book_info',
                            rps_rates=[20,40,60],
                            cpu_policies=[50],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/bookinfo/bandit-50',
                            pod_filter='productpage',
                            duration=120,
                            num_iters=25,
                            wait_time=120,
                            reset_cluster=False
                        )



# 2. Fixed Rate Workload (Out of Sample)
eval_cfg_cpu_fr_oos = EvalConfig(
                            name='fixed_rate_oosample',
                            services=cfg.services, 
                            deployments=cfg.deployments,
                            cpu_requests=600,
                            mem_requests=2000,

                            host='http://35.232.246.231/productpage',
                            locustfile='load_generator/locustfiles/bookinfo/default.py',
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            min_nodes=1,
                            max_nodes=60,

                            application='bookinfo',
                            rps_rates=[150,250], 
                            cpu_policies=[10,30,50,70,90],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/bookinfo/bandit-50',
                            pod_filter='productpage',
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

                            host='http://35.232.246.231/productpage',
                            locustfile='load_generator/locustfiles/bookinfo/default.py',
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            min_nodes=1,
                            max_nodes=60,

                            application='bookinfo',
                            rps_rates=[100,200,400,200,100], 
                            cpu_policies=[10,30,50,70,90],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/bookinfo/bandit-50',
                            pod_filter='productpage',
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

                            host='http://35.232.246.231/productpage',
                            locustfile='load_generator/locustfiles/bookinfo/default.py',
                            cluster_name='cola2',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='ob-pool',
                            min_nodes=1,
                            max_nodes=60,

                            application='bookinfo',
                            rps_rates=[150,250,350,250,150], 
                            cpu_policies=[10,30,50,70,90],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/bookinfo/bandit-50',
                            pod_filter='productpage',
                            duration=600,
                            num_iters=1,
                            wait_time=0,
                            reset_cluster=False
                        )


