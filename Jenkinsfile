pipeline {
        agent {
                dockerfile {
                      args '--network=$NETWORK_NAME \
                      	-e NEO4J_USER=$NEO4J_USER \
                      	-e NEO4J_PASSWORD=$NEO4J_PASSWORD \
                      	-e NEO4J_URL=$NEO4J_URL \
                      	-e NEO4J_BOLT_URL=$NEO4J_BOLT_URL'
                }
        }
        environment {
                CI = 'true'
        }
        stages {
                stage('Test') {
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
