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

# DBaas vs. DIY

### What is the case?
A short overview of the things you might need to think of when a database is necessary and giving you the choice of hosting a database server on you cluster, versus having one of the big cloud providers serve you one, as a DB as a service.

Traditionally, a database is hosted within the IT infrastructure of an organization. Until the beginning of this century we are talking about SQL based databases which were introduced over 50 years ago. When the cloud server possibilities were created, from lets say 15 years ago, also IaaS, PaaS, SaaS, and DBaaS come into view. Nowadays it is for a lot of organizations (probably the majority) the first choice when there is a need for databases in their data landscape.

### What to think of?
But is this always the case? You cannot answer this question without a thorough analysis of the prerequisites of the required solution, the current IT infrastructure of the organization, and a clear, well-thought IT strategy.

### A DbaaS might be the better choice if this is important:
- Lower amount of work and costs for setup, initialization of a database.
- Lower costs of maintenance, without the need for internal expertise.
- Easy and thus lower costs of backup/restore, maintenance and tuning, being done by the cloud provider.
- A easy to configure replication over multiple zones.
- Higher operational costs are acceptable.

### Organizations might make the better choice for a self-hosted, self-managed database:
- It might be more cost efficient, with the same specifications of the underlying platform, the costs for servers and software are lower.
- If there is a need for more choice on database flavors, like **MariaDB**, **MongoDB**, and **Oracle DB**.
- Full control is necessary over the setup and configuration.
- More control over where data is being kept, so more control over sovereignty and data privacy.
- DB knowledge will be needed with the organization, which of course is more costly but less chance on vendor lock-in.

### My opinion?
To my personal opinion especially the last points on sovereignty, privacy and vendor lock-in should have a higher priority. The balance between knowledge, costs, and sovereignty is often overlooked.