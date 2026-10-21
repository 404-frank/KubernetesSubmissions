# MongoDB backup cronjob

### deployment of the secret:
The connection to the Google storage bucket is done by using an SA account.
After creation of the account, create a key, download it as a JSON file, and create a secret like this:
```
kubectl create secret generic storage-sa-key --from-file=<key_file.json>
```
The key "storage-sa-key" is being using and mounted as a file in the backup pod.

### the further deployment is included in the kustomization.yaml!
### but if you really want, separate deployment being done with:

```
kubectl apply -f mongodb_backup_cronjob.yaml
```

