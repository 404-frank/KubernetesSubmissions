## Actionsn for a clean setup of the cluster.

### lets start with the cluster creation:
With my account I got issues with not enough resources being available, so I scaled down the number of nodes to '2'.
```
gcloud container clusters create dwk-cluster --zone=europe-west4 --cluster-version=1.37 --disk-size=32 --num-nodes=2 --machine-type=e2-small

check with:
kubectl cluster-info
```

### make sure the GKE cluster is the default (used to switch around a bit)
```
first check what the current context is:
kubectl config current-context
if necessary
kubectl config get-contexts
kubectl config use-context <new context>

```

### we need the namespace for deployment of ping-pong:
```
kubectl create namespace project
```

### deployed 'the project':
```
in the root, run:
kubectl apply -k .
```

### check the assigned IP address:
```
kubectl get svc
```


### Deletion
After use, this will get rid of the cluster again:
```
delete the cluster:
gcloud container clusters delete dwk-cluster --zone=europe-west4
```