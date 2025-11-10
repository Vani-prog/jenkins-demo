pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone your GitHub repo
                git branch: 'main', url: 'https://github.com/Vani-prog/jenkins-demo.git'
            }
        }

        stage('Setup') {
            steps {
                echo 'Checking Python version...'
                sh 'python3 --version'
            }
        }

        stage('Run') {
            steps {
                echo 'Running Python program...'
                sh 'python3 hello_world.py'
            }
        }
    }

    post {
        success {
            echo 'Python script executed successfully!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
