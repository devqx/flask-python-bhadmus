pipeline {
 agent any
  stages {
    stage("build iage"){
     when {
       branch 'master'
     }
     steps {
      script {
        app = docker.build('devxy/python_app')
      }
     }
    }
  }
}
