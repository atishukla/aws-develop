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

- Step 4: Start the testing for lambda
```
sam local invoke GetEc2RegionsFunction --no-event

(venv) atishukla@atishay:~/projects/aws-develop/serverless$ sam local invoke GetEc2RegionsFunction --no-event
Invoking main.lambda_handler (python3.7)
Image was not found.
Building image.........................................................................................................................................................................................................................................................................................................................................................................................................................................
Skip pulling image and use local one: amazon/aws-sam-cli-emulation-image-python3.7:rapid-1.10.0.

Mounting /home/atishukla/projects/aws-develop/serverless/get-ec2-regions as /var/task:ro,delegated inside runtime container
START RequestId: 4a2a8500-e20b-10ca-5f07-b3c768f3139c Version: $LATEST
[ERROR] ClientError: An error occurred (UnauthorizedOperation) when calling the DescribeRegions operation: You are not authorized to perform this operation.
Traceback (most recent call last):
  File "/var/task/main.py", line 8, in lambda_handler
    response = ec2.describe_regions()
  File "/var/runtime/botocore/client.py", line 316, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/var/runtime/botocore/client.py", line 635, in _make_api_call
    raise error_class(parsed_response, operation_name)
END RequestId: 4a2a8500-e20b-10ca-5f07-b3c768f3139c
REPORT RequestId: 4a2a8500-e20b-10ca-5f07-b3c768f3139c  Init Duration: 497.86 ms        Duration: 253.34 ms     Billed Duration: 300 ms Memory Size: 128 MB     Max Memory Used: 51 MB

{"errorType":"ClientError","errorMessage":"An error occurred (UnauthorizedOperation) when calling the DescribeRegions operation: You are not authorized to perform this operation.","stackTrace":["  File \"/var/task/main.py\", line 8, in lambda_handler\n    response = ec2.describe_regions()\n","  File \"/var/runtime/botocore/client.py\", line 316, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n","  File \"/var/runtime/botocore/client.py\", line 635, in _make_api_call\n    raise error_class(parsed_response, operation_name)\n"]}
```

As you can see from above it takes time to download docker image for the first time
Also I get an error for not having permission

Fix: Added EC2 policy to the aws user used in cli and not its a success

```
(venv) atishukla@atishay:~/projects/aws-develop/serverless$ sam local invoke GetEc2RegionsFunction --no-event
Invoking main.lambda_handler (python3.7)
Skip pulling image and use local one: amazon/aws-sam-cli-emulation-image-python3.7:rapid-1.10.0.

Mounting /home/atishukla/projects/aws-develop/serverless/get-ec2-regions as /var/task:ro,delegated inside runtime container

{"statusCode":200,"body":"{\"message\": [{\"Endpoint\": \"ec2.eu-north-1.amazonaws.com\", \"RegionName\": \"eu-north-1\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.ap-south-1.amazonaws.com\", \"RegionName\": \"ap-south-1\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.eu-west-3.amazonaws.com\", \"RegionName\": \"eu-west-3\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.eu-west-2.amazonaws.com\", \"RegionName\": \"eu-west-2\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.eu-west-1.amazonaws.com\", \"RegionName\": \"eu-west-1\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.ap-northeast-2.amazonaws.com\", \"RegionName\": \"ap-northeast-2\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.ap-northeast-1.amazonaws.com\", \"RegionName\": \"ap-northeast-1\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.sa-east-1.amazonaws.com\", \"RegionName\": \"sa-east-1\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.ca-central-1.amazonaws.com\", \"RegionName\": \"ca-central-1\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.ap-southeast-1.amazonaws.com\", \"RegionName\": \"ap-southeast-1\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.ap-southeast-2.amazonaws.com\", \"RegionName\": \"ap-southeast-2\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.eu-central-1.amazonaws.com\", \"RegionName\": \"eu-central-1\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.us-east-1.amazonaws.com\", \"RegionName\": \"us-east-1\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.us-east-2.amazonaws.com\", \"RegionName\": \"us-east-2\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.us-west-1.amazonaws.com\", \"RegionName\": \"us-west-1\", \"OptInStatus\": \"opt-in-not-required\"}, {\"Endpoint\": \"ec2.us-west-2.amazonaws.com\", \"RegionName\": \"us-west-2\", \"OptInStatus\": \"opt-in-not-required\"}]}"}
START RequestId: 452d2f9c-46cc-172c-876c-f8e8559fc7af Version: $LATEST
END RequestId: 452d2f9c-46cc-172c-876c-f8e8559fc7af
REPORT RequestId: 452d2f9c-46cc-172c-876c-f8e8559fc7af  Init Duration: 622.13 ms        Duration: 261.42 ms     Billed Duration: 300 ms Memory Size: 128 MB     Max Memory Used: 51 MB
```

- Test the API gateway
```
(venv) atishukla@atishay:~/projects/aws-develop/serverless$ sam local start-api
Mounting GetEc2RegionsFunction at http://127.0.0.1:3000/getec2regions [GET]
You can now browse to the above endpoints to invoke your functions. You do not need to restart/reload SAM CLI while working on your functions, changes will be reflected instantly/automatically. You only need to restart SAM CLI if you update your AWS SAM template
2020-11-15 21:59:45  * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
```
- Navigate to the endpoint and you will see all the regions

- Step 5: Package and deploy to AWS
We give S3 bucket for packging and added role for S3 to our role

```
sam package --template-file template.yaml --output-template-file deploy.yaml --s3-bucket atishay-sam-bucket
```
- Step 6 :
```
sam deploy --capabilities CAPABILITY_IAM --template-file deploy.yaml --stack-name SAMLamdaTestStack
```