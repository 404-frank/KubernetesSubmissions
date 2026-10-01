# todo-app, the mongo db for the backend
### it is using the persistent storage defined in "the_project"

### deployment being done with:


```
kubectl apply -f manifests/mongodb_secret.yaml
kubectl apply -f manifests/mongodb_service.yaml
kubectl apply -f manifests/mongodb_statefulset.yaml

or, all in once:
kubectl apply -f manifests/

```

