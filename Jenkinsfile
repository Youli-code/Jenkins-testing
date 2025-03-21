pipeline {
    agent any

    stages {
        stage('Greet') {
            steps {
                echo "👋 Hello, Youli! Welcome to Jenkins."
            }
        }

        stage('Run Bash Command') {
            steps {
                sh 'echo 🧪 Running a Bash command inside Jenkins!'
            }
        }

        stage('Goodbye') {
            steps {
                echo "🏁 Pipeline complete. Jenkinsfile works!"
            }
        }
    }

    post {
        always {
            echo "📜 This message runs at the end, no matter what."
        }
    }
}
