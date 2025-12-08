pipeline {
    agent any

    tools {
        allure 'allure'
    }

    stages {

        stage('Install Requirements') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    pip install -r /var/jenkins_home/workspace/HitAPI_Test/requirements.txt
                "
                '''
            }
        }

        stage('Run Test With Allure') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    pytest --alluredir=/var/jenkins_home/workspace/HitAPI_Test/allure-results /var/jenkins_home/workspace/HitAPI_Test
                "
                '''
            }
        }

    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }

}
