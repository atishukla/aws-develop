import boto3
import uuid

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create an organisation
orgId = str(uuid.uuid4())

table = dynamodb.Table('dynamo-test')
table.put_item(
    Item={
        'PK': f'ORG#{orgId}',
        'SK': f'#METADATA#{orgId}',
        'name': 'ABC Company',
        'tier': 'professional'
    }
)
