# DevopsProject
This project is a simple Django application that is deployed using a Continuous
Integration/Continuous Deployment (CI/CD) pipeline. The pipeline is implemented
using GitHub Actions, Docker, and Kubernetes. This project was made by Fatou Kiné
Ndiaye, Fama Sarr and Salimata Diagana.

## 1. Web Application Development
We developped a Django application with two differents
endpoints:
- [GET] **http:localhost:8000/users** endpoint returns the list of users in the databases (username, email, first
name and last name).
- [GET] **http:localhost:8000/visits** endpoint counts the number of visits of the website

and the home page at **http:localhost:8000** which is the page where the visits are counted.

## 2. Dockerisation
We wrote a Dockerfile for the Django application and use Docker
Compose to run the Django app and the Postgres DB in our local development
environment.

If you clone this repo, make sure to create a .env file at the root of the project based from the .env.template
file. Once you have the .env file, navigate to your project root (right where ```docker-compose.yaml``` is) and run:
```sh
docker-compose up -d
```
This will create the django app container and a persistent postgresql database running in the background. 
To bring this database down just run:
```sh
docker-compose down
```
Also in the root of your project run (on windows):
```sh
python3.9 -m venv env
env\Scripts\activate 
pip install -r web/requirements.txt
```
## 3. CI/CD Pipeline Setup
We mplemented a GitHub Actions workflow with two jobs : build-ci and deploy. Whenever changes
are pushed to the main branch or a pull request is made, the workflow
perform the following actions:
- Build the Docker image for the Django application:
  -  Install the dependencies
  - Check the code tests, linting and formatting
- Push the Docker image to docker hub
- Make the continuous deployment in kubernetes (with minikube since we don't have a kubernetes cluster)

## 4. Kubernetes deployment
We set up a local kubernetes cluster with minikube and the kubectl CLI. To deploy, we created app-configmap.yml
and app-secret.yml files to keep environment and secrets variables. Then, we created the deployments and services
with all the specification for django and postgres.

To test the kubernetes configurations in local follow these commands :

Start the node :
```sh
minikube start
```

First create configmap and secrets
```sh
kubectl apply -f app-configmap.yml,app-secret.yml
```

Create the deployments and services
```sh
kubectl apply -f django.yml,postgres.yml
```

Get the ressources (deployments, pods, services, replicasets)
```sh
kubectl get all
```

Access to the service outside the pods
```sh
minikube service django-service
```
