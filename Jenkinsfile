pipeline {
        agent {
                dockerfile {
                      filename 'Dockerfile'
                      args '-e NEO4J_USER=neo4j -e NEO4J_PASSWORD=2DEdTR4ooXFOgShqUqSOYWyLcfMgVcDx'
                }
        }
        environment {
                CI = 'true'
        }
        stages {
                stage('Test') {
                        steps {
                                sh 'python ./main_wrapper.py'
                        }
                }
        }
}
