pipeline {
    agent any

    stages {
        stage('Run Test 1') {
            steps {
                echo 'Running the first python script...'
                sh 'python3 test1.py'
            }
        }

        // THIS IS THE NEW PART
        stage('Run Loop') {
            steps {
                echo 'Running the loop script...'
                sh 'python3 loop1.py'
            }
        }
    }
}
