pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-id')
        IMAGE_NAME = "fareed798/wishlist-proj" 
        TAG = "${env.BRANCH_NAME}" 
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building image for version: ${TAG}"
                    bat "docker build -t ${IMAGE_NAME}:${TAG} ."
                }
            }
        }
        stage('Push to DockerHub') {
            steps {
                script {
                    echo "Pushing image to DockerHub..."
                    bat "echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin"
                    bat "docker push ${IMAGE_NAME}:${TAG}"
                }
            }
        }
    }
}