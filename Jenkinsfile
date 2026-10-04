pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
            python3 -m venv venv
            ./venv/bin/pip install -r requirements.txt
            '''
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/python -m unittest discover -v'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('SonarQube') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=jenkins-sonarqube-docker \
                            -Dsonar.sources=. \
                            -Dsonar.tests=. \
                            -Dsonar.test.inclusions=test_*.py \
                            -Dsonar.exclusions=test_*.py
                        """
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
