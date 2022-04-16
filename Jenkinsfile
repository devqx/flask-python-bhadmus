pipeline {
 agent any
  stages {
    stage("build iage"){
     when {
       branch 'master'
     }
     steps {
       docker.build('devxy/python_app')
     }
    }
  }
}
