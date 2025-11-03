pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup and Test') {
            agent {
                docker {
                    image 'python:3.12-slim'
                    args '--network jenkins-net'
                }
            }
            steps {
                sh '''
                    apt-get update && apt-get install -y python3-venv
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest --maxfail=1 --disable-warnings -q --html=reports/report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}
