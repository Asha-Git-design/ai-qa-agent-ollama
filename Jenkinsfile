pipeline {
    agent any

    tools {
        allure 'allure'
    }

    stages {
        stage('Clone Repo') {
            steps {
                // ✅ Specify branch explicitly to avoid "Couldn't find revision" error
                git branch: 'main', url: 'https://github.com/Asha-Git-design/ai-qa-agent-ollama.git'
            }
        }

        stage('Create Virtual Env') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Behave Tests') {
            steps {
                bat 'call venv\\Scripts\\activate && behave > behave-output.txt'
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
