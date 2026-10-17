# todo-app

### deployment being done with Kustomize:

```
kubectl apply -k .
```

### other handy commands:

```
show what would be done, for testing:
kubectl kustomize .

delete all again:
kubectl delete -k .

inspect on the cluster, use an extra pod:
kubectl run -it --rm test --image=busybox --restart=Never --env="POD_NAMESPACE=project"  -- sh

```

