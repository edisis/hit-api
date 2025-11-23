pipeline {
    agent any

    stages {  
        stage('Setup Environment') {
            steps {
                echo "Setting up virtual environment inside python-runner..."
                sh '''
                    docker exec python-runner bash -c "
                        python3 -m venv venv &&
                        . venv/bin/activate &&
                        pip install --upgrade pip &&
                        pip install -r requirements.txt
                    "
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo "Running pytest inside python-runner..."
                sh '''
                    docker exec python-runner bash -c "
                        . .venv/bin/activate &&
                        pytest --maxfail=1 --disable-warnings -q
                    "
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed."
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
        failure {
            echo "Some tests failed."
        }
        success {
            echo "All tests passed successfully."
        }
    }
}