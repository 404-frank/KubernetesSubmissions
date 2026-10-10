# log output app

### deployment being done with:

### deployment of the persistent volume is being done with:
```
(for deployment to GFE, only the claim is necessary, skip the volume itself)
kubectl apply -f manifests/persistentvolume.yaml
kubectl apply -f manifests/persistentvolumeclaim.yaml
```

### and the deployment of the services, ingress, and containers:
#### (with this deployment, also the pingpong container is included)

```
kubectl apply -f manifests/configmap.yaml
kubectl apply -f ../ping_pong/manifests/configmap.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f ../ping_pong/manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
kubectl apply -f manifests/deployment.yaml
```

### Exercise 3.3, move from ingress to gateway API
### and the deployment of the configmaps, services, gateway, routes, and containers:
#### (with this deployment, also the pingpong container is included)

```
kubectl apply -f manifests/configmap.yaml
kubectl apply -f ../ping_pong/manifests/configmap.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f ../ping_pong/manifests/service.yaml
kubectl apply -f manifests/gateway.yaml
kubectl apply -f ../ping_pong/manifests/route.yaml
kubectl apply -f manifests/route.yaml
kubectl apply -f manifests/deployment.yaml

kubectl config set-context --current --namespace=exercises

```
