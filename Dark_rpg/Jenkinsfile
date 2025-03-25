pipeline {
    agent any

    stages {
        stage('Run Dark in Docker') {
            steps {
                echo '🐳 Building and Running Dark RPG inside Docker container...'
                sh 'docker build -t dark-rpg .'
                sh 'docker run --rm dark-rpg > dark_run.log'
            }
        }

        stage('Archive Logs') {
            steps {
                echo '📦 Archiving logs for future reference...'
                archiveArtifacts artifacts: 'dark_run.log', onlyIfSuccessful: true
            }
        }
    }

    post {
        success {
            echo '✅ Victory! Dark RPG completed successfully.'
        }
        failure {
            echo '❌ The shadows consumed the build...'
        }
    }
}
