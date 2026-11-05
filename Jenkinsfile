pipeline {
    agent any
    environment {
        REGISTRY = "localhost:5000"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }
    stages {
        stage('Build and Push') {
            steps {
                sh 'docker build -t $REGISTRY/kk-payments:$IMAGE_TAG ./app'
                sh 'docker push $REGISTRY/kk-payments:$IMAGE_TAG'
            }
        }
        stage('Deploy to Staging') {
            steps {
                sh 'kubectl set image deployment/kk-payments kk-payments=$REGISTRY/kk-payments:$IMAGE_TAG -n kijani-staging'
                sh 'kubectl rollout status deployment/kk-payments -n kijani-staging --timeout=60s'
            }
        }
        stage('Staging Smoke Test') {
            steps {
                sh '''
                    PORT=$(kubectl get svc kk-payments -n kijani-staging -o jsonpath='{.spec.ports[0].nodePort}')
                    IP=$(minikube ip)
                    curl -s -f http://$IP:$PORT/health || (echo "Smoke test failed!" && exit 1)
                '''
            }
        }
        stage('Approval for Production') {
            steps {
                input(message: "Staging smoke test passed. Promote to Production?", ok: "Deploy to Prod")
            }
        }
        stage('Deploy to Production') {
            steps {
                sh 'kubectl create namespace default --dry-run=client -o yaml | kubectl apply -f -'
                sh 'kubectl set image deployment/kk-payments kk-payments=$REGISTRY/kk-payments:$IMAGE_TAG -n default'
                sh 'kubectl rollout status deployment/kk-payments -n default --timeout=60s'
            }
        }
    }
}
