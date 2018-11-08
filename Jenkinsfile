def label = "worker-${UUID.randomUUID().toString()}"

podTemplate(label: label, yaml: """
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: python
spec:
  volumes:
  - name: docker_socket
    hostPath:
      path: /var/run/docker.sock
  containers:
  - name: python
    image: python:3.7-slim
    command:
    - cat
    tty: true
  - name: docker
    image: docker:latest
    volumeMounts:
    - name: docker_socket
      mountPath: /var/run/docker.sock
    command:
    - cat
    tty: true
""") {
  node(label) {
      def repo = checkout scm
      def gitCommit = repo.GIT_COMMIT
      def gitBranch = repo.GIT_BRANCH
      def shortGitCommit = "${gitCommit[0..10]}"
    stage('Test') {
      container('python') {
        sh "pip install --upgrade pip & pip install neo4j-driver"
        sh "python ./src/tmp.py"
        sh "apt-get update && apt-get install -y curl"
	sh "curl neodb-service.default.svc.cluster.local:7474"
      }
    }
    stage('Build Docker image') {
      container('docker') {
        sh "docker build -t neopython_loader ."
      }
    }
  }
}
