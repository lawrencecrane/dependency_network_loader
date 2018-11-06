pipeline {
        agent {
                dockerfile {
                      args '-e NEO4J_USER=$NEO4J_USER \
                      	-e NEO4J_PASSWORD=$NEO4J_PASSWORD \
                      	-e NEO4J_URL=http://localhost:7474 \
                      	-e NEO4J_BOLT_URL=bolt://localhost:7687'
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
