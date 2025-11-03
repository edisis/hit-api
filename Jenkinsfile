pipeline {
    agent any
    
    stages {
        stage('Copy Test Files') {
            steps {
                sh '''
                    echo "Copying test files to Python container..."
                    docker exec python-runner rm -rf /app/tests/
                    docker cp . python-runner:/app/
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'docker exec python-runner pip install requests pytest allure-pytest'
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