# todo-app

### deployment being done with:
```
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/ingress.yaml
kubectl apply -f manifests/service-nodeport.yaml
kubectl apply -f manifests/service.yaml
```
### bringing down again with:
```
kubectl delete -f manifests/deployment.yaml
```