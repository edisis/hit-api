pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate && pip install --upgrade pip
                    . .venv/bin/activate && pip install -r requirements.txt
                '''
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