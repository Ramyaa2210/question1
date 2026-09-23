pipeline {
    agent { label 'windows' } // Ensures this runs on your Windows agent

    stages {
        stage('Checkout') {
            steps {
                // Pulls the latest code from your GitHub repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate & pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate & pytest test_app.py
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 Build Succeeded! All tests passed perfectly.'
        }
        failure {
            echo '❌ Build Failed! One or more unit tests failed.'
        }
    }
}
