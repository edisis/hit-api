pipeline {
    agent any
    
    stages {
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