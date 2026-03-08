# ACEest Fitness & Gym API

This repository contains a **Flask-based REST API** for a fitness and gym application, complete with **Docker support, automated testing, and CI/CD pipelines** via GitHub Actions and Jenkins.

---

## Repository Contents

- **Source Code:** `app.py`, `requirements.txt`  
- **Test Suite:** `tests/test_app.py`  
- **Infrastructure as Code:** `Dockerfile`, `.github/workflows/main.yml`  
- **Documentation:** `README.md`

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

## Docker Setup

1. **Build Docker image**
    ```bash
    docker build -t aceest-gym:latest .
2. **Run Docker container**
    ```bash
    docker run -d -p 5000:5000 aceest-gym:latest

Access the API at http://localhost:5000/

## Running Tests Manually
1. **Navigate to tests folder**
    ```bash
    cd tests
2. **Run Pytest**
    ```bash
    pytest test_app.py
This will execute all API endpoint tests and display results.

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

## Notes
Ensure Python 3.10+ is installed for local execution.
Docker is required for containerized testing.
Jenkins and GitHub Actions pipelines provide automated validation, so manual build steps are optional once configured.

