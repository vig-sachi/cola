import os

def gcloud_authentication():
    """
    Login to google cloud on machine, enabling CLI interface to cloud provider.
    """
    os.system('gcloud auth login')
    return


def set_project(project='vig-cloud'):
    """
    Set the project to use within Google Cloud.

    Args:
        project (str, optional): Name of project. Defaults to 'vig-cloud'.
    """
    os.system('gcloud config set project {}'.format(project))
    return


def create_cluster(project='vig-cloud', cluster='cola-test', zone='us-central1-c'):
    """
    Create a cluster on Google Kubernetes Engine with:
        - An application node pool for logging, monitoring, etc. pods.
        - An application node pool for app microservice deployments.

    Args:
        project (str, optional): Name of the project which hosts the cluster. Defaults to 'vig-cloud'.
        cluster (str, optional): Name of the GKE cluster. Defaults to 'cola-test'.
        zone (str, optional): Zone in which cluster is located. Defaults to 'us-central1-c'.
    """

    # Basic cluster information.
    cmd = 'gcloud beta container --project "{}" clusters create "{}" --zone "{}" '.format(project, cluster, zone)

    # First Node pool for non-application pods.
    cmd += '--no-enable-basic-auth --cluster-version "1.21.9-gke.1002" --release-channel "regular" --machine-type "e2-highmem-8" --image-type "COS_CONTAINERD" --disk-type "pd-standard" --disk-size "100" '
    cmd += '--metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring",'
    cmd += '"https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" '
    cmd += '--max-pods-per-node "110" --num-nodes "3" --logging=SYSTEM,WORKLOAD --monitoring=SYSTEM --enable-ip-alias --network "projects/{}/global/networks/default" --subnetwork "projects/{}/regions/us-central1/subnetworks/default" '.format(project, project)
    cmd += '--enable-intra-node-visibility --default-max-pods-per-node "110" --enable-dataplane-v2 --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing,GcePersistentDiskCsiDriver --enable-autoupgrade --enable-autorepair '
    cmd += '--max-surge-upgrade 1 --max-unavailable-upgrade 0 --enable-managed-prometheus --enable-shielded-nodes --node-locations "us-central1-c" '

    # Second Node pool for application pods.
    cmd += '&& gcloud beta container --project "{}" node-pools create "app-pool" --cluster "{}" --zone "{}" --machine-type "n1-standard-1" --image-type "COS_CONTAINERD" --disk-type "pd-standard" --disk-size "100" '.format(project, cluster, zone)
    cmd += '--metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring",'
    cmd += '"https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" '
    cmd += '--num-nodes "3" --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0 --max-pods-per-node "110" --node-locations "us-central1-c"'

    # Run cluster creation.
    os.system(cmd)
    return


def enable_istio_cluster(project='vig-cloud', cluster='cola-test', zone='us-central1-c', profile='demo'):
    """
    Enables istio on a cluster on Google Kubernetes Engine.

    Args:
        project (str, optional): Name of the project which hosts the cluster. Defaults to 'vig-cloud'.
        cluster (str, optional): Name of the GKE cluster. Defaults to 'cola-test'.
        zone (str, optional): Zone in which cluster is located. Defaults to 'us-central1-c'.
    """
    # Add admin permissions to current gcloud user.
    os.system('kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user={}'.format(os.popen('gcloud config get-value core/account').read().replace('\n','')))

    # Download and install Istio.
    os.system('curl -L https://git.io/getLastestIstio | sh -')

    # Install istio with given profile.
    os.system('istioctl install --set profile={} -y'.format(profile))

    # Enable auto sidecar injection for default namespace.
    os.system('kubectl label namespace default istio-injection=enabled')

    return

def authenticate(cluster='cola2', project='vig-cloud', zone='us-central1-c'):
    """
    Authenticate to a GKE cluster.

    Args:
        cluster (str, optional): Name of the GKE cluster. Defaults to 'cola2'.
        project (str, optional): Name of the project which hosts the cluster. Defaults to 'vig-cloud'.
        zone (str, optional): Zone in which cluster is located. Defaults to 'us-central1-c'.
    """
    os.system('gcloud container clusters get-credentials {cluster} --zone {zone} --project {project}'.format(cluster=cluster, zone=zone, project=project))
    return


def scale_node_pool(cluster='cola2', project='vig-cloud', zone='us-central1-c', node_pool='ob-pool', num_nodes=0):
    """
    Scale a node pool in GKE.

    Args:
        cluster (str, optional): Name of the GKE cluster. Defaults to 'cola2'.
        project (str, optional): Name of the project which hosts the cluster. Defaults to 'vig-cloud'.
        zone (str, optional): Zone in which cluster is located. Defaults to 'us-central1-c'.
        node_pool (str, optional): Name of the node pool to scale. Defaults to 'ob-pool'.
        num_nodes (int, optional): Number of nodes to scale node pool to. Defaults to 0.
    """
    os.system('gcloud container clusters resize {cluster} --zone {zone} --project {project} --node-pool {node_pool} --num-nodes {num_nodes} --quiet'.format(cluster=cluster, zone=zone, project=project, node_pool=node_pool, num_nodes=num_nodes))
    return


def enable_node_pool_autoscaling(cluster='cola2', project='vig-cloud', zone='us-central1-c', node_pool='ob-pool', min_nodes=1, max_nodes=10):
    """
    Enable cloud provider cluster autoscaling in GKE.

    Args:
        cluster (str, optional): Name of the GKE cluster. Defaults to 'cola2'.
        project (str, optional): Name of the project which hosts the cluster. Defaults to 'vig-cloud'.
        zone (str, optional): Zone in which cluster is located. Defaults to 'us-central1-c'.
        node_pool (str, optional): Name of the node pool to scale. Defaults to 'ob-pool'.
        min_nodes (int, optional): Minimum nodes in cluster. Defaults to 1.
        max_nodes (int, optional): Maximum nodes in cluster. Defaults to 10.
    """
    os.system('gcloud container clusters update {cluster} --enable-autoscaling --min-nodes {min_nodes} --max-nodes {max_nodes} --project {project} --zone {zone} --node-pool {node_pool}'.format(cluster=cluster, zone=zone, project=project, node_pool=node_pool, min_nodes=min_nodes, max_nodes=max_nodes))
    return


def disable_node_pool_autoscaling(cluster='cola2', project='vig-cloud', zone='us-central1-c', node_pool='ob-pool'):
    """
    Disable cloud provider cluster autoscaling in GKE.

    Args:
        cluster (str, optional): Name of the GKE cluster. Defaults to 'cola2'.
        project (str, optional): Name of the project which hosts the cluster. Defaults to 'vig-cloud'.
        zone (str, optional): Zone in which cluster is located. Defaults to 'us-central1-c'.
        node_pool (str, optional): Name of the node pool to scale. Defaults to 'ob-pool'.
    """
    os.system('gcloud container clusters update {cluster} --no-enable-autoscaling --project {project} --zone {zone} --node-pool {node_pool}'.format(cluster=cluster, zone=zone, project=project, node_pool=node_pool))
    return
