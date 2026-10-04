pipeline {
    agent any

    tools {
        sonarQubeScanner 'SonarScanner'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Unit Tests') {
            steps {
                sh 'python3 -m unittest discover -v'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('SonarQube') {
                        sh '''
                            sonar-scanner \
                              -Dsonar.projectKey=jenkins-sonarqube-docker \
                              -Dsonar.sources=. \
                              -Dsonar.tests=. \
                              -Dsonar.test.inclusions=test_*.py \
                              -Dsonar.exclusions=test_*.py
                        '''
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t shijo501/jenkins-sonarqube-docker:latest .'
            }
        }

        stage('Docker Hub Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login \
                          -u "$DOCKER_USER" --password-stdin
                        docker push shijo501/jenkins-sonarqube-docker:latest
                        docker logout
                    '''
                }
            }
        }
    }
}
