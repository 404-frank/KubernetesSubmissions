## Move log app to GitOps

### actions taken
- moved all necessary yampl files to manifests/base
- created production and statging overlays folders
- added namespaces for each of them
- updated mongodb cronjob yaml to be able to use "suspend"
- added switch to the backend to be able not to send to an external url, just log

### commands:
- kubectl apply -n argocd -f manifests/argocd-staging-app.yaml

- running the argoCD service:
```
- kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
- get the password:
- kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
- kubectl port-forward svc/argocd-server -n argocd 8080:443
```

- kustomize, staging or production:
```
cd the_project
kubectl apply -k manifests/overlays/staging/
kubectl apply -k manifests/overlays/production/
```


### results:

<!-- ![alt text](./screenshots/Screenshot_2026-11-04_21-37-15.png "ArgoCD") -->

