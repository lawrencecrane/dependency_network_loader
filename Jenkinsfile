pipeline {
        agent {
                dockerfile {
                      args '--network=$NETWORK_NAME'
                }
        }
        environment {
                CI = 'true'
        }
        stages {
                stage('Test') {
			environment {
                      		NEO4J_USER = "${env.NEO4J_USER}"
 		      		NEO4J_PASSWORD = "${env.NEO4J_PASSWORD}"
		      		NEO4J_URL = "${env.NEO4J_URL}"
		      		NEO4J_BOLT_URL = "${env.NEO4J_BOLT_URL}"
			}
                        steps {
				sh 'echo $NEO4J_USER'
				sh 'echo $NEO4J_PASSWORD'
				sh 'echo $NEO4J_URL'
				sh 'echo $NEO4J_BOLT_URL'
                                sh 'python /home/neo/main_wrapper.py'
                        }
                }
        }
}
