pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                // Jenkins does this automatically when you configure it later
            }
        }
        
        stage('Run Python') {
            steps {
                echo 'Running the Python script...'
                sh 'python3 test1.py'
            }
        }
    }
}
