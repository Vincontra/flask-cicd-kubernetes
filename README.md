# Flask CI/CD Pipeline with Docker, Kubernetes and GitHub Actions

## Project Overview

This project demonstrates a **complete CI/CD pipeline** for a Flask REST API application.

The pipeline automatically:

* Builds the application
* Runs automated tests
* Creates a Docker image
* Pushes the image to DockerHub
* Deploys the application to a Kubernetes cluster

The goal of this project is to show how modern **DevOps practices** can automate software delivery.

---

# Technologies Used

* Python (Flask)
* Docker
* Kubernetes (Minikube)
* GitHub
* GitHub Actions (CI/CD)
* Pytest (Testing)

---

# System Architecture

Developer → GitHub → GitHub Actions → DockerHub → Kubernetes → Running Application

Pipeline Flow:

1. Developer pushes code to GitHub
2. GitHub Actions pipeline starts automatically
3. Dependencies are installed
4. Tests are executed
5. Docker image is built
6. Image is pushed to DockerHub
7. Kubernetes pulls latest image and updates application

---

# Project Directory Structure

```
flask-cicd-project
│
├── app.py
├── requirements.txt
├── Dockerfile
├── test_app.py
│
├── k8s
│   ├── deployment.yaml
│   └── service.yaml
│
└── .github
    └── workflows
        └── cicd.yml
```

Explanation:

app.py
Main Flask REST API application.

requirements.txt
Python dependencies required for the project.

Dockerfile
Instructions to build Docker image.

test_app.py
Automated tests using pytest.

k8s/deployment.yaml
Kubernetes deployment configuration.

k8s/service.yaml
Kubernetes service configuration to expose the application.

.github/workflows/cicd.yml
GitHub Actions pipeline configuration.

---

# Flask Application

The application is a simple **Task Manager API**.

API Endpoints:

GET /
Returns application status message.

GET /tasks
Returns list of tasks.

POST /tasks
Creates a new task.

PUT /tasks/<id>
Marks a task as completed.

DELETE /tasks/<id>
Deletes a task.

Example response:

{
"message": "Task Manager API running with CI/CD pipeline"
}

---

# Step 1: Install Required Tools

Install the following tools:

Docker
kubectl
Minikube
Git
Python

Update system:

sudo apt update

Install Docker:

sudo apt install docker.io

Start Docker:

sudo service docker start

Add user to docker group:

sudo usermod -aG docker $USER

---

# Step 2: Start Kubernetes Cluster

Start Minikube:

minikube start --driver=docker

Verify cluster:

kubectl get nodes

Expected output:

minikube   Ready

---

# Step 3: Build Docker Image

Build Docker image:

docker build -t flask-cicd-app .

Run container:

docker run -p 5000:5000 flask-cicd-app

Open browser:

http://localhost:5000

---

# Step 4: Deploy Application to Kubernetes

Load Docker image into Minikube:

minikube image load flask-cicd-app

Deploy application:

kubectl apply -f k8s/deployment.yaml

Create service:

kubectl apply -f k8s/service.yaml

Check pods:

kubectl get pods

Check services:

kubectl get svc

---

# Step 5: Access Application

Run:

minikube service flask-service

A browser window will open with the application URL.

Example:

http://127.0.0.1:38037

---

# Step 6: Push Code to GitHub

Initialize repository:

git init

Add files:

git add .

Commit code:

git commit -m "Initial project"

Add remote repository:

git remote add origin <repository-url>

Push code:

git push -u origin main

---

# Step 7: Configure GitHub Actions CI/CD Pipeline

Create workflow file:

.github/workflows/cicd.yml

Pipeline performs:

1. Checkout repository
2. Setup Python
3. Install dependencies
4. Run tests
5. Build Docker image
6. Push image to DockerHub

Pipeline triggers automatically when code is pushed to main branch.

---

# Step 8: DockerHub Integration

Create DockerHub access token.

Add GitHub repository secrets:

DOCKER_USERNAME
DOCKER_PASSWORD

Pipeline logs in to DockerHub and pushes the image.

Example image:

dockerhubusername/flask-cicd-app:latest

---

# Step 9: Kubernetes Deployment Configuration

deployment.yaml defines:

* Number of replicas
* Container image
* Container port
* Image pull policy

Important configuration:

imagePullPolicy: Always

This ensures Kubernetes always pulls the latest image.

---

# Continuous Deployment Flow

Developer changes code → Push to GitHub

GitHub Actions pipeline automatically:

1. Runs tests
2. Builds Docker image
3. Pushes image to DockerHub

Then Kubernetes updates the running application.

---

# How to Verify the Pipeline Works

Follow these steps to test the CI/CD pipeline.

Step 1
Open application URL in browser.

Example response:

{
"message": "Task Manager API running with CI/CD pipeline"
}

Step 2
Modify the Flask application.

Example change in app.py:

return jsonify({"message": "CI/CD Pipeline Test Version 2"})

Step 3
Push the change to GitHub:

git add .
git commit -m "Testing CI/CD update"
git push

Step 4
Open GitHub repository → Actions tab.

You will see the pipeline running.

Steps executed:

Checkout code
Install dependencies
Run tests
Build Docker image
Push image to DockerHub

Step 5
Restart Kubernetes deployment:

kubectl rollout restart deployment flask-app

Step 6
Refresh the browser.

New output will appear:

{
"message": "CI/CD Pipeline Test Version 2"
}

This confirms the pipeline works correctly.

---

# Advantages of CI/CD

Faster development cycles
Automated testing
Reliable deployments
Reduced human errors
Continuous software delivery

---

# Conclusion

This project successfully demonstrates a **complete CI/CD pipeline** using:

Flask
Docker
Kubernetes
GitHub Actions

The pipeline automates building, testing, containerization, and deployment of the application.

This setup reflects real-world DevOps workflows used in modern cloud-native applications.
