pipeline {
   agent any

   parameters {
           booleanParam(defaultValue: false, description: "Enable service?", name: "myBoolean")
           string(defaultValue: "TEST", description: "Which environment to deploy in?", name: "deployEnv")
           choice(choices: ["TEST", "DEV", "QA", "PRE-PROD", "PROD"], description: "Which environment to deploy in?", name: "deployEnvChoice")
   }

   stages {
       stage("Demo"){
           steps {
               echo "myBoolean is set to ${params.myBoolean}."
               echo "deployEnv is set to ${params.deployEnv}."
               echo "deployEnvChoice is set to ${params.deployEnvChoice}."
           }
       }
   }
}
