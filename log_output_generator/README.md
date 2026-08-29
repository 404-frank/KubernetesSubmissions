# log output app, generator and listener

### deployment being done with:
```
kubectl apply -f manifests
```

### Comments
deployment.yaml will create two containers in the pod:

- log-output-generator-container
- log-output-listener-container

both containers share a shared volume on /usr/src/app/files