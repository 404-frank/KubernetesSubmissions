# todo-app

### deployment being done with:

### deployment of the persistent volume is being done with:
```
kubectl apply -f manifests/persistentvolume.yaml
kubectl apply -f manifests/persistentvolumeclaim.yaml
```

### and the deployment of the service, ingress, and containers:
#### (with this deployment)

```
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
kubectl apply -f manifests/deployment.yaml
```

