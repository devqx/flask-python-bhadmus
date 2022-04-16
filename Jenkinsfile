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
   
   stage('Push image to repository'){
    docker.withRegistry('https://registry.hub.docker.com', 'docker_login'){
     app.push("${env.BUILD_NUMBER}")
      app.push("latest")
    }
   }
   
   
  }
}
