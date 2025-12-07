pipeline {
    agent any

    tools {
        allure 'allure'
    }

    stages {

        steps {
            sh '''
            docker exec python-runner bash -c "
                pip install -r /var/jenkins_home/workspace/HitAPI/requirements.txt
            "
            '''
        }
    }

    stage('Run Test With Allure') {
        steps {
            sh '''
            docker exec python-runner bash -c "
                pytest /var/jenkins_home/workspace/HitAPI/allure-results
            "
            '''
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
    
}
