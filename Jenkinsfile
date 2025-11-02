pipeline {
    agent {
        docker { 
            image 'python:3.12-slim' 
        }
    }
    
    stages {
        stage('Setup') {
            steps {
                sh 'python -m venv .venv'
                sh '. .venv/bin/activate && pip install --upgrade pip'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '. .venv/bin/activate && pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}