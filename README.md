## Run

1. Build docker image based on Dockerfile

```sh
eval $(minikube docker-env)  # To enter minikube docker enviroment
docker build -t sample-app:latest -f sample-app/Dockerfile .
```

## Ingress

### To install Ingress Controller in minikube:

```sh
minikube addons enable ingress
```

It automatically starts the K8s Nginix implementation of Ingress Controller.
That's one of many 3rd party impelmentation of Ingress controller

### Run Flask application

```sh
pip install -r requirements.txt
flask --app sample-app/sample-app.py run
```

## Additional

### Remove all docker images where repository = <none>

```sh
python -m clean_none_docker_images
```
