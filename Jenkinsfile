pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
              withAWS(credentials: 'my-aws-id', region: 'us-east-1') {
                sh 'python3 createS3bucket.py'
              }
            }
        }
        stage('Uploas') {
          steps {
            withAWS(credentials: 'my-aws-id', region: 'us-east-1') {
             s3Upload(file:'file.txt', bucket:'big-thing-happen-big1', path:'file.txt')
            }
          }
        }
    }
}

// pipeline {
//     agent any

//     stages {
//         stage('Hello') {
//             steps {
//               withAWS(credentials: 'aws-creds', region: 'us-east-1') {
//                 sh 'python3 createS3bucket.py'

//               }
//             }
//         }
//         stage('upload to s3') {
//           steps{
//             dir('') {
//               pwd():
//               withAWS(credentials: 'aws-creds', region: 'us-east-1') {
//                 def identity=awsIdentity():
//                 s3Upload(bucket:"big-thing-happen-big1", workingDir:'', includePathPatten:'**/*')
//               }
//             }
//           }
//         }
//     }
// }

