## Solution:

I spinned up the Google cluster again. And in the meantime I removed all request and limts again from the code as I think these are not necessary for the project at this time.

See below for all actions taken

I looked around in the GKE dashboard and was able to find the logs, here is how it looked when adding a todo:


![alt text](https://raw.githubusercontent.com/404-frank/KubernetesSubmissions/refs/tags/3.12/chapter4/exercise_3.12/screenshots/Screenshot_2026-10-23_15-06-35.png "the log output")


***

## Actions taken:

### lets start with the cluster creation:
With my account I got issues with not enough resources being available, so I scaled down the number of nodes to '2'.
```
gcloud container clusters create dwk-cluster --zone=europe-west4 --cluster-version=1.37 --disk-size=32 --num-nodes=2 --machine-type=e2-small

check with:
kubectl cluster-info
```

### enable the gateway
```
gcloud container clusters update dwk-cluster --location=europe-west4 --gateway-api=standard
```

### we need the namespace for deployment of the project:
```
kubectl create namespace project
```

### check the assigned IP address:
```
kubectl get svc
```

### deployed 'the project':
```
in the root, run:
kubectl apply -k .
```

### Deletion
After use, this will get rid of the cluster again:
```
delete the cluster:
gcloud container clusters delete dwk-cluster --zone=europe-west4
```