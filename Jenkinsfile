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
     
    steps {
       input('deploy to production?')
       withKubeConfig([
        credentialsId: 'kubeconfig',
        serverUrl: 'https://ad2fb861-a5a1-4942-a02e-69be955047bf.vultr-k8s.com:6443'
       ]) {
           sh 'kubectl apply -f deploy.yml'
       }
    }
   
   }
   
  }
}
