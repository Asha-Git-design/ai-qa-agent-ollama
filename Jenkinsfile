pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                // your steps here
            }
        }

        stage('Create Virtual Env') {
            steps {
                // your steps here
            }
        }

        stage('Install Dependencies') {
            steps {
                // your steps here
            }
        }

        stage('Run Behave Tests') {
            steps {
                // your steps here
            }
        }

        stage('Allure Report') {
            steps {
                // already added steps to generate report
            }
        }
    }

    // ✅ This goes here
    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}