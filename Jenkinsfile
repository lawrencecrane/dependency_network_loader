def label = "worker-${UUID.randomUUID().toString()}"

podTemplate(label: label, containers: [
  containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true),
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
]) {
  node(label) {
      def repo = checkout scm
      def gitCommit = repo.GIT_COMMIT
      def gitBranch = repo.GIT_BRANCH
      def shortGitCommit = "${gitCommit[0..10]}"
    stage('Build Docker image') {
      container('docker') {
        sh "docker build -t neopython_loader ."
      }
    }
  }
}
