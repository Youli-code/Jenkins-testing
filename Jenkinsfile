pipeline {
    agent any

    stages {
        stage('Run DARK') {
            steps {
                echo "🧙‍♂️ Launching the Dark RPG..."
                sh 'python3 dark.py --auto --script master_script.txt'
            }
        }
    }

    post {
        always {
            echo "🎮 Game run complete."
        }
    }
}

