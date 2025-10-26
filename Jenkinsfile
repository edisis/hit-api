pipeline {
    agent any

    environment {
        VENV_PATH = ".venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh """
                    python3 -m venv ${VENV_PATH}
                    ${VENV_PATH}/bin/pip install --upgrade pip
                    ${VENV_PATH}/bin/pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    source ${VENV_PATH}/bin/activate
                    pytest -v --disable-warnings --maxfail=1
                """
            }
        }
    }

    post {
        always { echo 'Pipeline Completed' }
        success { echo 'All Test Passed' }
        failure { echo 'Some Tests Failed' }
    }
}
