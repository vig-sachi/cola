from utils.config import EvalConfig
from configs.app.online_boutique.config import cfg



##############################################
#### Evaluations
##############################################

# 1. Fixed Rate Workload (In Sample)
eval_cfg = EvalConfig(
                            name='fixed_rate_insample2',
                            services=cfg.services, 
                            deployments=cfg.deployments,
                            cpu_requests=500,
                            mem_requests=1900,

                            host='',
                            locustfile='microservices/online_boutique/workloads/default.py',
                            cluster_name='cola-test-ob',
                            project_name='vig-cloud',
                            zone='us-central1-c',
                            node_pool='app-pool-2',
                            min_nodes=1,
                            max_nodes=130,

                            application='online_boutique',
                            rps_rates=[200,250,300],
                            cpu_policies=[30,50,70],
                            bandit_policy='50_ms',
                            train_config_path='/home/packard2700/autoscale-bandit/models/online_boutique/bandit-50',
                            pod_filter='frontend',
                            duration=60,
                            num_iters=15,
                            wait_time=120,
                            reset_cluster=False,

                            deployment_path = 'microservices/online_boutique/deployments.yaml',
                            gateway_path = 'microservices/online_boutique/gateway.yaml',
                            pods_per_node = 1,
                            cluster_type = 'default',                            
                        )
