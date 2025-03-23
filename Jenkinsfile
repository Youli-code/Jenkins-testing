pipeline {
    agent any

    stages {
        stage('Run Dark with Logs') {
            steps {
                echo '⚔️ Running Dark RPG in auto mode, capturing output...'
                // Run the game & capture all console output in dark_run.log
                sh 'python3 dark.py --auto --script master_script.txt > dark_run.log'
            }
        }

        stage('Archive Logs') {
            steps {
                echo '📦 Archiving logs for future reference...'
                archiveArtifacts artifacts: 'dark_run.log', fingerprint: true
            }
        }
    }

    post {
        always {
            echo '🎉 Pipeline complete!'
        }
    }
}

