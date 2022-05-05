# COLA - Learned Autoscalers for Kubernetes

COLA is a python package that trains and runs learned **autoscalers** for Kubernetes. These autoscalers differ from those built in to Kubernetes in a couple of key ways:

- COLA optimizes for latency and cost, not machine utilization.
  - COLA is trained to optimize the number of microservice replicas in your cluster to satisfy a latency constraint which you provide (e.g. a median end to end latency of 50ms) at the lowest cost across a set of application workloads.
- COLA adapts its policy to your application's workload.
  - COLA, once trained, runs in inference mode where it observes your applications current workload and applies an optimized autoscaling policy.

<!-- Typical results and link to paper -->

## Installation

Once you clone the repository `git clone https://github.com/vig-sachi/cola.git` install dependencies based on your operating system:

### Debian
    python3 dependencies/install_deb.py

Here's a full list of what's installed:

### Mac
    python3 dependencies/install_mac.py

Here's a full list of what's installed:

## Setting up a Kubernetes Cluster

<!-- Describe Dependencies -->

<!-- Cluster Diagram -->


### Google Kubernetes Engine (GKE)

<!-- Setup VM -->

<!-- Graphic of the setup (from istio gke telemetry) -->

<!-- Creating Sample Application -->

<!-- Verifying things worked -->


## COLA Training

<!-- Settings for training (latency target, workloads) -->

<!-- Running training -->

<!-- Tracking progress -->


## COLA Evaluation

<!-- Settings for evaluation (workloads) -->

<!-- Running evaluation for comparables -->

<!-- Running evaluation for comparables -->

<!-- Viewing results for evaluation -->


## COLA Inference 

<!-- Running COLA in inference mode -->

<!-- Tracking policy changes and workloads -->

