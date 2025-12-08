pipeline {
    agent any

    environment {
        TELEGRAM_BOT_TOKEN = '8313140175:AAFHhvYESd6PxhvweTsLZgcnHsGwdS2x6VM'
        TELEGRAM_CHAT_ID  = '619908852'
        WORKSPACE_PATH    = '/var/jenkins_home/workspace/HitAPI_Test'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies in docker container..."
                sh """
                    docker exec python-runner pip install -r ${WORKSPACE_PATH}/requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests with Allure results..."
                sh """
                    docker exec python-runner pytest -v --alluredir=${WORKSPACE_PATH}/allure-results ${WORKSPACE_PATH}
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo "Generating Allure report..."
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }

        stage('Send Telegram Notification') {
            steps {
                script {
                    def status = currentBuild.result ?: 'SUCCESS'
                    def message = """
Build #${env.BUILD_NUMBER} for job ${env.JOB_NAME} finished with status: ${status}

Allure Report: ${env.BUILD_URL}allure/
Jenkins Console: ${env.BUILD_URL}console
                    """.replaceAll("'", "'\\\\''")

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
                def message = """
Build #${env.BUILD_NUMBER} for job ${env.JOB_NAME} FAILED!

Jenkins Console: ${env.BUILD_URL}console
                """.replaceAll("'", "'\\\\''")

                sh """
                curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage \
                    -d chat_id=${TELEGRAM_CHAT_ID} \
                    -d text='${message}'
                """
            }
        }
    }
}
