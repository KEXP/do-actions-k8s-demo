## actions-k8s-flask-demo

simple POC for leveraging gh actions to build a simple flask app into a new deployment with the private container registry into the kubernetes cluster for donor portal

# Code

Simple flask app that prints out the hostname of the system the app is running on. This means upon each refresh, you can see different hostnames which proves the app is being distributed across all nodes in the cluster and being loadbalanced accordingly. Requirements file added for good measure.

# Dockerfile

Simple image. Take code, copy in....build. yay

# Config dir

1. deployment yaml: defines the flask app deployment in kubernetes
2. loadbalancer yaml: defines the load balancer object used for the flask deployment in kubernetes

# Actions

workflow.yaml

- github action sees a file being watched has been updated
- using a runner (ubnunt-latest), the code is pulled in, the necessary tools to interface with DO are installed
- a new image is built using the newly pushed code
- that new image is then pushed to the container registry at DO and named with the git-sha given during the code checkin
- that image is then used to rolling update the live deployment in kubernetes
- the status of the deployment is verified
