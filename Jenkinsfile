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
        stage('Uploas') {
          steps {
            s3Upload acl: 'Private', bucket: 'big-thing-happen-big1', cacheControl: '', excludePathPattern: '', file: 'file.txt', includePathPattern: '', metadatas: [''], path: 'Prudential-test-s3/file.txt', redirectLocation: '', sseAlgorithm: '', tags: '', text: 'the people of Georgia', workingDir: '/Prudential-test-s3/file.txt'
          }
        }
    }
}

// pipeline {
//     agent any

//     stages {
//         stage('Hello') {
//             steps {
//               withAWS(credentials: 'aws-creds', region: 'us-east-2') {
//                 sh 'python3 createS3bucket.py'

//               }
//             }
//         }
//         stage('upload to s3') {
//           steps{
//             dir('') {
//               pwd():
//               withAWS(credentials: 'aws-creds', region: 'us-east-2') {
//                 def identity=awsIdentity():
//                 s3Upload(bucket:"big-thing-happen-big1", workingDir:'', includePathPatten:'**/*')
//               }
//             }
//           }
//         }
//     }
// }

