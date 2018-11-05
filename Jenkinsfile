pipeline {
        agent {
                dockerfile {
                      args '-e NEO4J_USER=neo4j -e NEO4J_PASSWORD=2DEdTR4ooXFOgShqUqSOYWyLcfMgVcDx -e NEO4J_URL=http://neodb:7474 -e NEO4J_BOLT_URL=bolt://neodb:7687 --network=neonet'
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
