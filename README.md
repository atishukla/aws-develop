# aws-develop
This will contain learning for development on aws

### Serverless Function requirement

- SAM -> Serverless Application Model
- With SAM you can test the application locally
- AWS CLI
- Docker  (For Testing)
- unzip
- SAM CLI (pip install aws-sam-cli) Done in virtualenv
```
(venv) atishukla@atishay:~$ sam --version
SAM CLI, version 1.10.0
```
- Create a IAM user with Pragmatic access and configure aws client
This is used for testing
```
(venv) atishukla@atishay:~/projects/aws-develop$ aws configure
AWS Access Key ID [None]: <key>
AWS Secret Access Key [None]: <key>
Default region name [None]: eu-west-2
Default output format [None]: json
(venv) atishukla@atishay:~/projects/aws-develop$
```
- Actual lambda will use the role we specify in template.yaml

### Steps

- Step 1: Go to the desired folder

- Step 2: 
```

(venv) atishukla@atishay:~/projects/aws-develop/$ sam init --runtime python3.7 --name serverless
Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1

Project name [sam-app]: serverless

Cloning app templates from https://github.com/awslabs/aws-sam-cli-app-templates.git

AWS quick start application templates:
        1 - Hello World Example
        2 - EventBridge Hello World
        3 - EventBridge App from scratch (100+ Event Schemas)
        4 - Step Functions Sample App (Stock Trader)
Template selection: 1

-----------------------
Generating application:
-----------------------
Name: serverless
Runtime: python3.7
Dependency Manager: pip
Application Template: hello-world
Output Directory: .

Next steps can be found in the README file at ./serverless/README.md
```

- Step 3: Edit template.yaml as per your folder and function
Reference : https://github.com/aws/serverless-application-model/blob/master/versions/2016-10-31.md
