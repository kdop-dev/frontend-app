# front-app

## Criar helm

```bash
helm create front-app
```

## Instalar

Teste

```bash
helm template --namespace adsantos front-app ./front-app --dry-run --debug
```

Pra valer

```bash
helm install --namespace adsantos --create-namespace front-app ./front-app
```

### Atualizar

```bash
helm upgrade --namespace adsantos front-app ./front-app
```

### Excluir

```bash
helm delete --namespace adsantos front-app
```

Verificando

```bash
kubectl get all -n adsantos

```

```bash
kubectl logs -f pod/front-app-64d4d4b788-kkc98 -n adsantos # funciona até reiniciar o pod

kubectl logs -f -l app.kubernetes.io/name=front-app -n adsantos # funciona sempre
```