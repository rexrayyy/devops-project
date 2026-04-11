pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t myapp:${BUILD_NUMBER} .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run myapp:${BUILD_NUMBER} python -m pytest tests/ -v'
            }
        }   
        stage('Deploy') {
            steps {
                sh 'docker stop myapp || true'
                sh 'docker rm myapp || true'
                sh 'docker run -d --name myapp -p 5000:5000 myapp:${BUILD_NUMBER}'
            }
        }
        
    }
    post {
    success {
        echo 'Pipeline успешно выполнен!'
    }
    failure {
        echo 'Pipeline упал, проверь логи!'
    }
}
}