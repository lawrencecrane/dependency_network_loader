def label = "worker-${UUID.randomUUID().toString()}"

podTemplate(label: label, containers: [
  containerTemplate(name: 'python', image: 'python:3.7-slim', command: 'cat', ttyEnabled: true,
		    envVars: [
            	      envVar(key: 'NEO4J_URL', value: 'http://neodb-service:7474'),
            	      envVar(key: 'NEO4J_BOLT_URL', value: 'bolt://neodb-service:7687'),
		      secretEnvVar(key: 'NEO4J_USER', secretName: 'neo4j-auth-secret', secretKey: 'neo4j-user'),
	              secretEnvVar(key: 'NEO4J_PASSWORD', secretName: 'neo4j-auth-secret', secretKey: 'neo4j-pw')
        	    ]),
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
    stage('Test') {
      container('python') {
        sh "pip install --upgrade pip & pip install neo4j-driver"
        sh "python ./src/main_wrapper.py"
      }
    }
    stage('Build Docker image') {
      container('docker') {
        sh "docker build -t neopython_loader ."
      }
    }
  }
}
