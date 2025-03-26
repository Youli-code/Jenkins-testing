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

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker Image...'
                sh 'docker build --no-cache -t dark-rpg .'
            }
        }

        stage('Run Game in Auto Mode') {
            steps {
                echo '🎮 Launching Dark RPG (auto mode)...'
                sh 'docker run --rm dark-rpg'
            }
        }

        stage('Archive Logs') {
            steps {
                echo '📦 Archiving logs for future reference...'
                archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            echo '✅ Victory! Dark RPG completed successfully.'
        }
        failure {
            echo '💀 The pipeline failed. The darkness consumes us...'
        }
    }
}
