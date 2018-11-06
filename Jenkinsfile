pipeline {
        agent {
                dockerfile {
                      args '-p 7474:7474 \
			-p 7687:7687 \
			-e NEO4J_USER=$NEO4J_USER \
                      	-e NEO4J_PASSWORD=$NEO4J_PASSWORD \
                      	-e NEO4J_URL=http://172.17.72.179:7474 \
                      	-e NEO4J_BOLT_URL=bolt://172.17.72.179:7687'
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
