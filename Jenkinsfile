pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}/Dark_rpg"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Run Game in Auto Mode') {
            steps {
                sh 'python -m Dark_rpg.main --auto --script Dark_rpg/master_script.txt'
            }
        }

        stage('Post Run Cleanup') {
            steps {
                echo 'RPG test run complete!'
            }
        }
    }

    post {
        failure {
            echo 'The realm has fallen! Check logs for clues.'
        }
        success {
            echo 'Victory! The game ran as expected.'
        }
    }
}
