pipeline {
    agent {
        docker { image 'node:8.11.3-alpine' }
    }

    stages {
        stage('Build') {
            steps {
                sh 'node --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
