# containerize-your-application-project-group-4-go-gonzales-labre
containerize-your-application-project-group-4-go-gonzales-labre created by GitHub Classroom

# CryptoCurrently

CryptoCurrently is an application that aims to provide trend indicators through quantified sentiments from Twitter to Cryptocurrency traders, primarily traders who are inexperienced and are unable to put great time and effort into trading. Users will be able to view Cryptocurrency-related information based on social media sentiments. These sentiments will be extracted from a specific number of tweets from Twitter and will generate the visuals that show relevant information regarding the currency. Users will be able to switch through specific currencies to view information. The app serves to be an indicator and information app, any decision leading up to investment is entirely up to the user. 


## Getting Started

These instructions will help you deploy the CryptoCurrently project on Kubernetes, where it describes the process of the creation of pods, services, ingress, and autoscaling of the pods.

### Prerequisites

The system requirements include Python 3.0 or higher, PIP, Git, and Docker

#### For Python:

Can be installed via https://www.python.org/downloads/

#### For PIP:

Can be installed on Linux, Max via

```
python -m ensurepip --upgrade
```

Can be installed on Windows via

```
python -m ensurepip --upgrade
```

#### For Git:

Can be installed on Linux via

```
sudo apt update
sudo apt upgrade
sudo apt install git
```

Can be installed on Mac via

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew doctor
brew install git
```

Can be installed on Windows via

```
 https://gitforwindows.org/
```

#### For Docker:

Can be installed on Linux via https://docs.docker.com/desktop/install/linux-install/
Can be installed on Mac via https://docs.docker.com/desktop/install/mac-install/
Can be installed on https://docs.docker.com/desktop/install/windows-install/

### Installing

Users can choose to either pull from Dockerhub or from GitHub. 

#### Follow these steps to pull from GitHub: 

1. Ensure Git is installed correctly:

```
git —version
```

2. Clone the repository:

```
git clone https://github.com/admu-zaavedra/containerize-your-application-project-group-4-go-gonzales-labre.git
```

3. Create python virtual environment:

```
python -m venv venv
Python -m virtualenv venv
```

4. To install necessary packages:

```
pip install -r requirements.txt 
Run python nltk.py
```

5. Create .env file with the following variables: 

```
SECRET_KEY = '<any randomized keygen>' 
DB_NAME = 'cryptodb' 
DB_USER = 'postgres' 
DB_PASS = 'postgres'
```

6. Setup local database (path: projcryptocurrently/resources):

```
psql -U [username] -f setup.sql
```

7. To run the server locally with no problems:

```
python manage.py runserver --noreload
```

#### Follow these steps to pull from DockerHub: 

1. Ensure Docker is installed correctly:

```
docker —version
```

2. Pull from Docker:

```
docker pull miguelgg1024/cryptocurrentlyamdnew
```

3. Create docker container for image:

```
docker create miguelgg1024/cryptocurrentlyamdnew
If using Docker Desktop, click play/run image and set targetport to 8080
```

4. Go to https://localhost:8080/ on web browser to run container



## Deployment to Kubernetes

App is deployed on Kubernetes using image from DockerHub.

#### Via Google Cloud Platform:

1. Enable Kubernetes API:
From menu, click Kubernetes and enable API if prompted

2. Create cluster:
Create Cluster from Kubernetes menu

3. In cloud shell, set env variables:
```
export my_zone=<name_of_region> export my_cluster=<name_of_cluster>
```

4. Configure kubectl tab completion:
```
source <(kubectl completion bash)
```

5. Configure access to cluster:
```
gcloud container clusters get-credentials $my_cluster --zone $my_zone
```

6. Clone the repository to Cloud Lab:
```
git clone https://github.com/admu-zaavedra/containerize-your-application-project-group-4-go-gonzales-labre.git
```

7. Change to project root directory:
```
cd ~/projcryptocurrently/
```

8. Deploy kubernetes deployment manifest:
```
kubectl apply -f ./cryptocurrently-deployment.yaml
```

9. Deploy kubernetes service manifest
```
kubectl create -f cryptocurrency-deployment.yaml --save-config
kubectl expose deployment cryptocurretnly-deployment --target-port=8080 --type=NodePort
```

10. Configure application for autoscaling
```
kubectl autoscale deployment cryptocurrency-deployment --max 4 --min 1 --cpu-percent 25
```

11. Deploy loadgen container
```
kubectl apply -f loadgen.yaml
```

12. Scale loadgen deployment
```
kubectl scale deployment loadgen --replicas 0
```

13. Create pods for dns-demo
```
kubectl apply -f dns-demo.yaml
```

14. Deploy v1 manifest:
```
kubectl create -f cryptocurrently-v1.yaml
```
15. Deploy service manifest:
```
kubectl apply -f ./cryptocurrently-svc.yaml
```

16. Deploy nodeport manifest:
 ```
kubectl apply -f ./cryptocurrently-nodeport-svc.yaml
```

17. Reserve Google Cloud Networking Static IP Addresses:
Click on Networking -> IP Addresses -> Reserve External Static Address
Create one regional-loadbalancer
Create one global-ingress

18. Deploy v2 manifest:
```
kubectl create -f cryptocurrently-v2.yaml
```

19. Save regional static ip address into env variable:
```
export STATIC_LB=$(gcloud compute addresses describe regional-loadbalancer --region us-central1 --format json | jq -r '.address')
```

20. Replace placeholder address in manifest:
```
sed -i "s/10\.10\.10\.10/$STATIC_LB/g" cryptocurrently-lb-svc.yaml
```

21. Deploy LoadBalancer service manifest:
```
kubectl apply -f ./cryptocurrently-lb-svc.yaml
```

22. Deploy ingress manifest:
```
kubectl apply -f cryptocurrently-ingress.yaml
```

23. Access via browser:
```
curl http://[external_IP]/v1
curl http://[external_IP]/v2
```


## Built With

* Natural Language Toolkit (NLTK) - NLP for the website
* Django - the web framework used


## Authors
* Kendra Kirsten Go
* Jose Miguel Gonzales
* David Andrew Labre


## Acknowledgments

Original code by:
Carl Jimson B. Ejaus - UI/UX Designer and Front-End Dev Lead, Developer
David Andrew J. Labre - Back-end Dev Lead, Developer
Mon Gabriel F. Lagustan - QA Lead and Systems Analyst, Developer
Kian Angelo M. Oladive - Main Developer
Jonas Raphael L. Palomo - Data Science Lead, Developer
Kyle Mark Victoriano - QA Lead, Project Manager

