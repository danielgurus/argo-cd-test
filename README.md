# systems_sandbox
Shared repo for working out systems concepts

I have a basic test that once we can get running, then we've proved out the basic setup.

There are two APIs:
- The REST API just tests to see if it connect to a specified service. I just put in GCS and Hazelcast for now, but then we'll add GraphDB, BigTable, Firestore, ElasticSearch when we're ready. 
    - They are FastAPI GET routes that return a 200 status code if they can connect to the service.
- The RPC API is intended to test out the Keda setup.
    - The API is also FastAPI, but they publish a message to a topic.
    - Keda then needs to listen to the topic and launch the appropriate function:
        - `GET .../launch_function_a` -> publishes message to `FUNCTION_A`
        - Keda listens for `FUNCTION_A` and launches the `service_a()` function
        - `service_a()` calls the RPC API `GET .../launch_function_b`
        - `.../launch_function_B` -> publishes message to `FUNCTION_B`
        - Keda listens for `FUNCTION_B` and launches the `service_b()` function
        - `service_b()` just prints out a message
        - if we see the `service_b` message in the logs, then we know that the APIs and functions are working

There are four docker files:
- REST API pointing to rest_main : 8000
- RPC API pointing to rpc_main : 8005
- Function A to be run via Keda
- Function B to be run via Keda

The docker files may not be 100% correct (the code as well) as I haven't had a chance to test this so feel free to fix anything that's wrong.



[click on the link for minukube setup](https://www.linuxbuzz.com/install-minikube-on-ubuntu/ )

# Instructions for Running sandbox-main Application in Minikube

This guide outlines the steps to deploy and run the sandbox-main application in Minikube along with troubleshooting steps for errors encountered while running Docker containers.

## Prerequisites

Ensure that the following dependencies are installed and running on your local machine:

- Docker
- Minikube

## Deployment Steps

### Step 1: Start Minikube
minikube start

### Step 2: Check Running Pods
kubectl get pod

### Step 3: Apply Deployment and Service Files
kubectl apply -f service.yaml
kubectl apply -f deployment.yaml

### Step 4: Expose the App Using LoadBalancer
kubectl create deployment balanced --image=wedge3d/platform-dev:latest
kubectl expose deployment balanced --type=LoadBalancer --port=8000

### Step5: In another terminal window, start the Minikube tunnel:
minikube tunnel

### Step6: Find Routable IP
kubectl get services balanced

### ABOVE command will provide the IP address and port number where the application is running. You can access the application using this IP and port number

### 

### NOTE : your docker file should be in the present directory while running below commands 

# STEPS FOR RUNNING DOCKER FILES INDIVIDUALLY
# STEPS FOR RUNNING RPC_API
docker build -t rpc-api .

# Running the Dockerfile of rpc_api
docker run -d -p 8000:8000 rpc-api

# To check running container 
docker ps -a

## WHEN YOU DO docker ps -a you can find the recently terminated container and check logs 
docker logs "container id " or "name"


# STEPS FOR RUNNING REST_API
docker build -t rest-api .

# Running the Dockerfile of rest_api
docker run -d -p 8001:8001 rest-api

# To check running container 
docker ps -a

## WHEN YOU DO docker ps -a you can find the recently terminated container and check logs 
docker logs "container id " or "name"


# NOTE: You should be running this commands where your docker files will be present  

# Docker Steps for building FUNCTION A
docker build -t function_a .

# Docker Steps for running FUNCTION A
docker run -d -p 3001:3001 function_a

# To check running container 
docker ps -a

## WHEN YOU DO docker ps -a you can find the recently terminated container and check logs 
docker logs "container id " or "name"

# Docker Steps for building FUNCTION A
docker build -t function_b .

# Docker Steps for running FUNCTION A
docker run -d -p 3002:3002 function_b

# To check running container 
docker ps -a

## WHEN YOU DO docker ps -a you can find the recently terminated container and check logs 
docker logs "container id " or "name"


# steps to install KEDA and run KEDA

# 1. Add Helm repo
helm repo add kedacore https://kedacore.github.io/charts
helm repo update

# 2. Install KEDA with hemm
helm install keda kedacore/keda

# 3. Verify KEDA Installation
kubectl get pods -n keda

# 4. Apply the ScaledObject
kubectl apply -f scaledobject.yaml
