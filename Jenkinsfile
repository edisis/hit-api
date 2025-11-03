pipeline {
    agent any
    
    stages {
        stage('Setup Python Environment') {
            steps {
                sh 'docker exec python-runner pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker exec python-runner pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}