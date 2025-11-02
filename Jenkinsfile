pipeline {
    agent any
    
    stages {
        stage('Setup Python Env') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install --upgrade pip'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run API Tests') {
            steps {
                sh '. .venv/bin/activate && pytest --maxfail=1 --disable-warnings -q --html=reports/test-report.html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}