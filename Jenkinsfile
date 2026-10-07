docker exec Jenkins sh -c "cat > /tmp/kubeconfig <<'EOF'
apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority: /tmp/ca.crt
    server: https://192.168.49.2:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    namespace: default
    user: minikube
  name: minikube
current-context: minikube
users:
- name: minikube
  user:
    client-certificate: /tmp/client.crt
    client-key: /tmp/client.key
EOF"
docker exec Jenkins sh -c "KUBECONFIG=/tmp/kubeconfig kubectl get nodes"
docker exec Jenkins sh -c "KUBECONFIG=/tmp/kubeconfig kubectl get nodes"
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/bhattrahul76660-cyber/cloud-support-devops-project.git'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t customer-ticket-api:latest .'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker stop customer-ticket-api || true'
                sh 'docker rm customer-ticket-api || true'
                sh 'docker run -d --name customer-ticket-api -p 5000:5000 customer-ticket-api:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    export KUBECONFIG=/tmp/kubeconfig
                    kubectl set image deployment/customer-ticket-api customer-ticket-api=customer-ticket-api:latest
                    kubectl rollout status deployment/customer-ticket-api
                '''
            }
        }
    }
}