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
    
    steps {
     script {
       docker.withRegistry('https://registry.hub.docker.com', 'docker_login'){
       app.push("${env.BUILD_NUMBER}")
       app.push("latest")
   }
    }
    }
  }
   
   stage('deploy to cluster'){
     
    input('deploy to production?')
    milestone(1)
    kubernetesDeploy(
     kubeconfigId: 'kubeconfig',
     configs: 'deploy.yml',
     enableConfigSubstitution: true
    )
   
   }
   
  }
}
