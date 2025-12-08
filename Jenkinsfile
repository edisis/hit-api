pipeline {
    agent any

    environment {
        TELEGRAM_BOT_TOKEN = '8313140175:AAFHhvYESd6PxhvweTsLZgcnHsGwdS2x6VM'
        TELEGRAM_CHAT_ID = '619908852'
    }

    stages {
        stage('Run Tests in Docker') {
            steps {
                script {
                    docker.image('python:3.13.9-slim').inside("--network jenkins-net -v jenkins_home:/var/jenkins_home") {
                        stage('Install Dependencies') {
                            sh '''
                                cd /var/jenkins_home/workspace/HitAPI_Test@script
                                pip install -r requirements.txt
                            '''
                        }
                        
                        stage('Run Tests') {
                            sh '''
                                cd /var/jenkins_home/workspace/HitAPI_Test@script
                                pytest test_api.py -v --alluredir=allure-results
                            '''
                        }
                    }
                }
            }
        }
        
        stage('Generate Report & Kirim Telegram') {
            steps {
                script {
                    // Generate Allure Report
                    allure includeProperties: false, 
                           jdk: '', 
                           results: [[path: 'allure-results']]

                    // Siapkan pesan Telegram
                    def allureReportUrl = "${env.BUILD_URL}allure/"
                    def status = currentBuild.result ?: 'SUCCESS'
                    
                    def summary = ''
                    try {
                        if (fileExists('allure-report/widgets/summary.json')) {
                            def summaryJson = readJSON file: 'allure-report/widgets/summary.json'
                            summary = """
Test Summary:
Total: ${summaryJson.statistic.total}
Passed: ${summaryJson.statistic.passed}
Failed: ${summaryJson.statistic.failed}
Broken: ${summaryJson.statistic.broken}
Skipped: ${summaryJson.statistic.skipped}
"""
                        }
                    } catch (Exception e) {
                        echo "Could not read summary: ${e.message}"
                        summary = ""
                    }
                    
                    def message = """
Test Automation Report

Job: ${env.JOB_NAME}
Build: #${env.BUILD_NUMBER}
Status: ${status}
Duration: ${currentBuild.durationString}
Date: ${new Date().format('dd-MM-yyyy HH:mm')}

${summary}Allure Report: ${allureReportUrl}
Jenkins Build: ${env.BUILD_URL}
                    """.replaceAll("'", "'\\\\''")
                    
                    // Kirim ke Telegram
                    sh """
                    curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage \
                    -d chat_id=${TELEGRAM_CHAT_ID} \
                    -d disable_web_page_preview=false \
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
Build Failed

Job: ${env.JOB_NAME}
Build: #${env.BUILD_NUMBER}

Console: ${env.BUILD_URL}console
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
