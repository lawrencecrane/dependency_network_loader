pipeline {
        agent {
  		kubernetes {
			label 'neo_python'
			defaultContainer 'jnlp'
			yamlFile 'neopython_pod.yaml'
		}
        }
        environment {
                CI = 'true'
        }
        stages {
                stage('Test') {
                        steps {
                                sh 'python /home/neo/main_wrapper.py'
                        }
                }
        }
}
