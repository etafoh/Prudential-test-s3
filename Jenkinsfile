pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
              withAWS(credentials: 'aws-creds', region: 'us-east-2') {
                sh 'python3 createS3bucket.py'

              }
            }
        }
    }
}

