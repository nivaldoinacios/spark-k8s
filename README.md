```sh
## operador
helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator
helm install spark spark-operator/spark-operator --namespace spark 
```

```sh
## serviceaccount
kubectl create serviceaccount spark

## clusterrole
k create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=spark:spark --namespace=spark
```

```sh
## tag and build
docker build . -t carlosbpy/spark-py:latest -f docker/dev.Dockerfile

## push
docker push carlosbpy/spark-py:latest
```

```sh
## apply manifest
kubectl apply -f manifests/spark-yaml -n spark
```

```sh
## see logs
k logs -f pyspark-k8s-driver -n spark
```