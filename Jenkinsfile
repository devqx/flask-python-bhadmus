pipeline {
 agent any
  stages {
    stage("build image"){
    
     steps {
      script {
        app = docker.build('devxy/python_app')
      }
     }
    }
  }
}
