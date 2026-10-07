## Actions;

### lets start with the cluster creation:
With my account I got issues with not enough resources being available, so I scaled down the number of nodes to '2'.
```
gcloud container clusters create dwk-cluster --zone=europe-west4 --cluster-version=1.37 --disk-size=32 --num-nodes=2 --machine-type=e2-small
```

### Do not forget to install the CLI, on the local pc:
```
sudo apt-get install google-cloud-cli-gke-gcloud-auth-plugin
```

### we need the namespace for deployment of ping-pong:
```
kubectl create namespace exercises
```

### deployed postgres:
see: postgres manifest folder ../postgres/manifests for the files:
apply all but persistentvolume.yaml

### and finally deployed the ping pong app:
```
kubectl apply -f manifests/configmap.yaml
kubectl apply -f manifests/loadbalancer.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/deployment.yaml
```

### and here we are:
![alt text](https://raw.githubusercontent.com/404-frank/KubernetesSubmissions/refs/tags/3.1/chapter4/exercise_3.1/screenshots/Screenshot_2026-10-07_20-39-07.png "the pings output")

![alt text](https://raw.githubusercontent.com/404-frank/KubernetesSubmissions/refs/tags/3.1/chapter4/exercise_3.1/screenshots/Screenshot_2026-10-07_20-39-25.png "the pingpong output")

### Deletion
After use, this will get rid of the cluster again:
```
delete the cluster:
gcloud container clusters delete dwk-cluster --zone=europe-west4
```