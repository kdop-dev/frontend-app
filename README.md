# Frontend-app

## run locally

```bash
cd app

./start.sh
```

## run with docker

```bash
./start.sh
```

## Testing locally

<http://127.0.0.1:5002/health>

## Install on kubernetes

```bash
helm upgrade --install --namespace adsantos --create-namespace front-app helm
```

### k8s

```bash
#export EXTERNAL_IP=$(kubectl get svc/ingress-nginx-controller -n ingress-nginx -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
export EXTERNAL_IP=$(kubectl get ingress/front-app -n adsantos -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')

curl --header "Host: learn.adsantos.io" http://$EXTERNAL_IP/adsantos/front-app/index
```

> locahost (for docker desktop) and public ip for cluster in the cloud.

### Browser

Add `EXTERNAL_IP` to `/etc/hosts`:

```hosts
127.0.0.1   learn.adsantos.io
```

And go to <http://learn.adsantos.io/adsantos/front-app/index>

```bash
open http://learn.adsantos.io/adsantos/front-app/index
```
