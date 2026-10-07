# postgress database

### deployment being done with:
```
secrets:
kubectl apply -f manifests/postgres_secret.yaml

persistent volume:
note: for GKE only activate the claim, not the volume itself.
kubectl apply -f manifests/persistentvolume.yaml
kubectl apply -f manifests/persistentvolumeclaim.yaml

service and postgres itself:
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/postgres_statefulset.yaml
```

After Postgres is up and running, follow the guidelines in 'populate_db.sql'.
