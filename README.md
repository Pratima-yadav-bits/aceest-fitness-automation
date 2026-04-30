# Aceest Fitness & Gym API

This repository contains a **Flask-based REST API** for a fitness and gym application, complete with **Docker support, automated testing, and CI/CD pipelines** via GitHub Actions and Jenkins.

---

## Repository Contents

- **Source Code:** `app.py`, `requirements.txt`  
- **Test Suite:** `tests/test_app.py`  
- **Infrastructure as Code:** `Dockerfile`, `.github/workflows/main.yml`  
- **Documentation:** `README.md`

---

## Version History

### V1 – Initial Version
- Implemented basic Flask application
- Added core endpoints:
  - /program
  - /program/<name>
- Established initial project structure
### V2 – Feature Enhancement
- Extended API with additional endpoints
- Introduced BMI calculation feature
- Integrated database for persistent storage
- Enhanced overall application capabilities

---

## Local Setup & Execution

1. **Clone the repository**

    ```bash
    git clone https://github.com/Pratima-yadav-bits/aceest-fitness-gym-devops.git
    cd aceest-fitness-gym-devops

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt

3. **Run the Flask application locally**
    ```bash
    python app.py

The API will be available at: http://127.0.0.1:5000/

---

## Docker Setup

1. **Build Docker image**
    ```bash
    docker build -t aceest-gym:latest .
2. **Run Docker container**
    ```bash
    docker run -d -p 5000:5000 aceest-gym:latest

Access the API at http://localhost:5000/

---

## Running Tests Manually
1. **Navigate to tests folder**
    ```bash
    cd tests
2. **Run Pytest**
    ```bash
    pytest test_app.py
This will execute all API endpoint tests and display results.

---

## CI/CD Pipeline Overview

### Jenkins
Jenkins server is configured to handle the primary build phase.
It pulls the latest code from GitHub and performs a clean build of the environment.
Serves as a secondary validation layer to ensure the code compiles and integrates correctly.

### GitHub Actions
Fully automated CI/CD pipeline configured via .github/workflows/main.yml.
Triggered on every push or pull request.
Stages executed:
1. **Build & Lint**: Check syntax and coding standards using pylint.
2. **Docker Image Assembly**: Build the Docker container for deployment.
3. **Automated Testing**: Run the Pytest suite inside the container to confirm functionality and stability.


| Endpoint          | Method | Description                            |
|-----------------  |--------|----------------------------------------|
| `/`               | GET    | Welcome message and available endpoints|
| `/programs`       | GET    | Returns all available programs         |
| `/program/<name>` | GET    | Returns details of a specific program  |
| `/clients`        | GET    | Returns all clients in the database    |
| `/add-client`     | POST   | Add a new client to the database       |
| `/bmi`            | GET    | Calculate BMI based on height & weight |

---


## Containerization with Docker & Docker Hub
The Flask application is containerized using Docker by creating images that include application code and dependencies. These images are versioned (v1, v2) and stored in Docker Hub for easy access and deployment.

### Implementation

1. **Build Docker Image (v1 / v2)**

   ```bash
   docker build -t aceest:v1 .
   docker build -t aceest:v2 .
	
2. **Login to Docker Hub**
	
	```bash
	docker login
	
3. **Tag Image for Docker Hub**
	
	```bash
	docker tag aceest:v1 pratimayadav289/aceest:v1
	docker tag aceest:v2 pratimayadav289/aceest:v2
	
4. **Push Image to Docker Hub**
	
	```bash
	docker push pratimayadav289/aceest:v1
	docker push  pratimayadav289/aceest:v2

### Outcome
- Images stored on Docker Hub
- Version control using tags (v1, v2)
- Easy deployment in Kubernetes

---

## Continuous Integration with Jenkins
Jenkins is used as the CI server to automate the build process. A Jenkinsfile defines pipeline stages and triggers builds automatically when code changes are detected in the Git repository.

### Implementation
1. Configure Jenkins Job
2. Connect GitHub repository
3. Enable SCM polling
4. Jenkinsfile (Pipeline Trigger)

### Outcome
- Automatic pipeline trigger on code push
- Continuous build execution
- Faster development cycle

---

## SonarQube Integration
SonarQube is integrated into the Jenkins pipeline to perform static code analysis and generate quality reports.

### Implementation
1. Run SonarQube (Docker)
2. Configure SonarQube in Jenkins
3. Install SonarQube plugin
4. Add SonarQube server in Jenkins config
5. Add SonarQube Stage in Jenkinsfile

### Outcome

- Automatic code quality analysis
- Detection of bugs, vulnerabilities, code smells
- Report generation in SonarQube dashboard

---

## Continuous Delivery and Deployment Strategies
This project demonstrates deployment of a Flask-based application using Kubernetes with Minikube. It showcases modern deployment strategies to ensure high availability and zero downtime.

### Deployment strategies implemented:

- **Blue-Green Deployment**
- **Canary Deployment**
- **Shadow Deployment**

### Minikube Cluster Setup
1. Start the Minikube cluster with required CPU and memory configuration.
2. Verify that the cluster is running successfully.
3. Confirm that Kubernetes node is available and ready.

### Deployment of Application (v1 & v2)
1. Build the Docker image for both the version (v1 & v2) of the application.
2. Load the image into the Minikube environment.
3. Deploy the application using Kubernetes deployment configuration.
4. Expose the application using a Kubernetes service.
5. Verify that pods and services are running successfully.

### Access Application
1. Expose the Kubernetes service externally using Minikube.
2. Open the application in a browser using the generated URL.
3. Verify that the application is working correctly.

---

### Blue-Green Deployment
Blue-Green deployment uses two identical environments:
- Blue (v1) - Live production environment
- Green (v2) - New version
Only one version serves user traffic at a time.

### Implementation
1. Deploy both v1 and v2 versions in the cluster.
2. Initially, route all traffic to v1 (Blue environment).
3. Validate the v2 application independently.
4. Update the service configuration to point to v2.
5. Verify that traffic is successfully switched to v2

### Result
1. Zero downtime deployment achieved
2. Instant rollback possible by switching back to v1

---

### Canary Deployment
Canary deployment gradually shifts traffic from the old version to the new version.

### Implementation

1. Deploy both v1 and v2 applications.
2. Configure v1 with higher replicas and v2 with fewer replicas.
3. Allow both versions to receive traffic simultaneously.
4. Monitor application performance and behavior.
5. Gradually increase traffic to v2 based on stability.

### Result
1. Controlled release of new version
2. Reduced deployment risk
3. Better monitoring and validation

---

### Shadow Deployment
Shadow deployment runs the new version in parallel without exposing it to users.

### Implementation
1. Deploy both v1 and v2 applications.
2. Expose only the v1 service to users.
3. Keep v2 running in the background without traffic.
4. Validate v2 internally without affecting users.

### Result
1. Safe testing of new version
2. No impact on production users

---

## Conclusion

This project demonstrates how a well-designed CI/CD pipeline can automate the entire software delivery process, from code integration to deployment. By integrating Jenkins, Docker, and Kubernetes, the system achieves high efficiency, reliability, and scalability. The use of advanced deployment strategies further enhances the ability to release updates safely and efficiently.

---