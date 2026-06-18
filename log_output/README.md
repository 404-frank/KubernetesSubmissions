# log output app

### deployment being done with:
```
kubectl apply -f manifests/deployment.yaml
```

# handy snippets:

#### show pods:
```
kubectl get pods
```

#### output: (two pods running)
![alt text](https://raw.githubusercontent.com/404-frank/KubernetesSubmissions/main/log_output/screenshots/Screenshot_2026-06-18_20-37-04.png "kubectl get pods output")


#### show logs:
```
kubectl logs -f log-output-deployment-78f558948b-zrc8n
replace the -f aargument with the actual name of the pod as seen above
```

#### output:
![alt text](https://raw.githubusercontent.com/404-frank/KubernetesSubmissions/main/log_output/screenshots/Screenshot_2026-06-18_20-39-03.png "kubectl logs -f log-output-deployment-78f558948b-zrc8n")

#### now fun starts, raise the numbers of replica's in the deployment.yaml:
#### deployment.yaml:
![alt text](https://raw.githubusercontent.com/404-frank/KubernetesSubmissions/main/log_output/screenshots/Screenshot_2026-06-18_20-39-55.png "deployment.yaml")

and apply the deployment:
```
kubectl apply -f manifests/deployment.yaml
```

#### funny isn't, two more pods are spinning up:
![alt text](https://raw.githubusercontent.com/404-frank/KubernetesSubmissions/main/log_output/screenshots/Screenshot_2026-06-18_20-40-37.png "four pods running")
