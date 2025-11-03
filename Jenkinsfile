pipeline {
    agent any
    
    stages {
        stage('Setup Python') {
            steps {
                sh '''
                    apt update && apt install -y python3 python3-pip python3-venv
                    python3 -m venv .venv
                    . .venv/bin/activate && pip install --upgrade pip
                    . .venv/bin/activate && pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
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