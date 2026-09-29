# postgress database

### deployment being done with:
```
secrets:
kubectl apply -f manifests/postgres_secret.yaml

persistent volume:
kubectl apply -f manifests/persistentvolume.yaml
kubectl apply -f manifests/persistentvolumeclaim.yaml

service and postgres itself:
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/postgres_statefulset.yaml
```
