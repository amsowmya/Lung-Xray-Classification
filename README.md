# DeepLearningEnd2End

aws configure


# Workflows

- constants
- config_entity
- artifact_entity
- components
- pipeline
- main

# Bentoml
- Model serving  -> Provide api's -> serving the model to the user
- Application packaging  -> bento.yaml -> Bento Image -> AWS, Azure
- Deployment


bentoml models list
bentoml serve service.py:service --reload
bentoml build

=====================================

bentoml build
bentoml containerize xray_service:latest -t 506234360787.dkr.ecr.us-east-2.amazonaws.com/xray_bento_image:latest
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 506234360787.dkr.ecr.us-east-2.amazonaws.com
docker push 506234360787.dkr.ecr.us-east-2.amazonaws.com/xray_bento_image:latest

# ######################################################################

1. Source code
2. Build Docker image
3. Push to the Docker hub
4. AWS EC2
5. IAM user
6. Launch docker to the EC2

Workflow (yaml)
- CI/CD/CD
- CI/CD - Github Action server
- CD - EC2 (as self hosted runner)

==========================================

###### Install Docker on EC2 machine #########

sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
ls
sudo sh get-docker.sh
docker --version
docker images
sudo usermod -aG docker ubuntu
newgrp docker
docker images

# ############ After installing Docker on EC2 ###########
Go to Gothub action -> settings -> Actions -> Runner -> Execute all commands from here