# distributor app

- depends on a nats server being deployed in the cluster
- using the_project configMap
- gets messages from nats queue
- todo messages are being send by the_project_backend to the queue


### deployment being done with:

```
kubectl apply -f deployment.yaml

```

