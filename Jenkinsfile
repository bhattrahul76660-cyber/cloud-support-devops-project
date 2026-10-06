pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/bhattrahul76660-cyber/cloud-support-devops-project.git'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t customer-ticket-api:latest .'
            }
        }

        stage('Docker Run') {
            steps {
                bat 'docker stop customer-ticket-api || exit 0'
                bat 'docker rm customer-ticket-api || exit 0'
                bat 'docker run -d --name customer-ticket-api -p 5000:5000 customer-ticket-api:latest'
            }
        }
    }
}
