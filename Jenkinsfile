pipeline {
    agent {
        docker {
            image 'python:3.13.9-slim'
            args '--network jenkins-net -v jenkins_home:/var/jenkins_home'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    cd /var/jenkins_home/workspace/HitAPI_Test@script
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    cd /var/jenkins_home/workspace/HitAPI_Test@script
                    pytest test_api.py -v --alluredir=allure-results
                '''
            }
        }

        stage('Generate Report & Kirim Telegram') {
            steps {
                script {
                    allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
                    def message = "Build #${env.BUILD_NUMBER} selesai, lihat report: ${env.BUILD_URL}allure/"
                    sh """
                    curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage \
                    -d chat_id=${TELEGRAM_CHAT_ID} \
                    -d text='${message}'
                    """
                }
            }
        }
    }

    post {
        failure {
            script {
                sh """
                curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage \
                -d chat_id=${TELEGRAM_CHAT_ID} \
                -d text='Build #${env.BUILD_NUMBER} gagal. Lihat console: ${env.BUILD_URL}console'
                """
            }
        }
    }
}
