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
                      		NEO4J_USER=$NEO4J_USER
 		      		NEO4J_PASSWORD=$NEO4J_PASSWORD
		      		NEO4J_URL=$NEO4J_URL
		      		NEO4J_BOLT_URL=$NEO4J_BOLT_URL
			}
                        steps {
                                sh 'python /home/neo/main_wrapper.py'
                        }
                }
        }
}
