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
					checkout([$class: 'GitSCM',
					branches: [[name: 'refs/tags/v1']],
					userRemoteConfigs: [[url: 'https://github.com/Pratima-yadav-bits/aceest-fitness-automation']]
					extensions: [[$class: 'CleanBeforeCheckout']]
				])
            }
        }

       stage('Detect Version') {
			steps {
				script {
					env.VERSION = "v1"
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
				bat 'py -m pytest --junitxml=report.xml'
			}
		}

        stage('Archive Test Results') {
            steps {
                junit 'report.xml'
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
            echo "Build Successful"
        }
        failure {
            echo "Build Failed"
        }
    }
}