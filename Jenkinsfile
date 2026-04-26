pipeline {
    agent any

    environment {
        IMAGE_NAME = "aceest"
    }

    triggers {
        pollSCM('H/5 * * * *')   // every 5 min check repo changes
    }

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Pratima-yadav-bits/aceest-fitness-automation'
            }
        }

        stage('Detect Version') {
            steps {
                script {
                    bat 'git fetch --tags'
                    def tag = bat(script: 'git describe --tags --abbrev=0', returnStdout: true).trim()
                    env.VERSION = tag ?: "latest"
                    echo "Version: ${env.VERSION}"
                }
            }
        }

        stage('Install Dependencies') {
			steps {
				bat '''
				py -m pip install --upgrade pip
				py -m pip install -r requirements.txt
				'''
			}
		}
        
		stage('Run Tests (Pytest)') {
			steps {
				bat 'py -m pytest test_app.py --junitxml=report.xml'
			}
		}

        stage('Archive Test Results') {
            steps {
                junit 'report.xml'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                        bat '''
                        sonar-scanner ^
                        -Dsonar.projectKey=aceest ^
                        -Dsonar.sources=. ^
                        -Dsonar.host.url=http://localhost:9000 ^
                        -Dsonar.login=%SONAR_TOKEN%
                        '''
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%VERSION% .'
            }
        }

        stage('Generate Artifact') {
            steps {
                bat 'docker save %IMAGE_NAME%:%VERSION% -o %IMAGE_NAME%_%VERSION%.tar'
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: '*.tar', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "Build Successful 🚀"
        }
        failure {
            echo "Build Failed ❌"
        }
    }
}