pipeline {
        agent {
		environment {
                      NEO4J_USER=$NEO4J_USER
 		      NEO4J_PASSWORD=$NEO4J_PASSWORD
		      NEO4J_URL=$NEO4J_URL
		      NEO4J_BOLT_URL=$NEO4J_BOLT_URL
		}
                dockerfile {
                      args '--network=$NETWORK_NAME'
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
