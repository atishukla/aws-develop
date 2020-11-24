import boto3
import uuid
import pprint
from datetime import datetime, timezone
from boto3.dynamodb.conditions import Key, Attr

# Get the service resource.
dynamodb = boto3.resource('dynamodb')


def create_organisation():
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


def create_project():
    # 2. Create an agile project in the organisation

    test_company_org_id = '0eb258f8-5d2c-425a-972a-acfb6c808fba'
    project_id = str(uuid.uuid4())

    table = dynamodb.Table('dynamo-test')
    table.put_item(
        Item={
            'PK': f'ORG#{test_company_org_id}',
            'SK': f'PRO#agile#{project_id}',
            'name': 'Project Y',
            'project_id': project_id
        }
    )


def create_employees():
    # 2. Create an agile project in the organisation

    abc_company_id = '0eb258f8-5d2c-425a-972a-acfb6c808fba'
    jane = str(uuid.uuid4())

    table = dynamodb.Table('dynamo-test')
    table.put_item(
        Item={
            'PK': f'ORG#{abc_company_id}',
            'SK': f'EMP#{jane}',
            'name': 'Jane Tuck',
            'email': 'jane@test.com'
        }
    )


def assign_employee_to_project():

    abc_company_id = '0eb258f8-5d2c-425a-972a-acfb6c808fba'
    project_x = '047e37cc-0987-47d4-bc9e-29cbdfe375bf'
    project_y = 'bcd5976e-173d-4445-a796-26b69bfff068'
    project_f = 'b3d87035-51f4-4a4a-a236-1dbd10fb383f'

    atishay = '2262ced5-e0d4-4137-81e2-faab82f5ef5b'
    john = ''
    jane = ''

    table = dynamodb.Table('dynamo-test')
    table.put_item(
        Item={
            'PK': f'ORG#{abc_company_id}#PRO#{project_x}',
            'SK': f'ORG#{abc_company_id}#EMP#{atishay}',
            'name': 'Atishay Shukla',
            'project': 'Project X',
            'date_of_join': datetime.now(timezone.utc).strftime('%c')
        }
    )


def create_fixed_bid_project():
    # 2. Create an Fixed bid project in the organisation

    test_company_org_id = 'a5a28161-14f7-480b-888a-a94e72bf8208'
    project_id = str(uuid.uuid4())

    table = dynamodb.Table('dynamo-test')
    table.put_item(
        Item={
            'PK': f'ORG#{test_company_org_id}',
            'SK': f'PRO#fixed-bid#{project_id}',
            'name': 'Project B',
            'project_id': project_id
        }
    )


def edit_organisation():
    test_company_org_id = 'a5a28161-14f7-480b-888a-a94e72bf8208'
    table = dynamodb.Table('dynamo-test')
    table.update_item(
        Key={
            'PK': f'ORG#{test_company_org_id}',
            'SK': f'#METADATA#{test_company_org_id}'
        },
        UpdateExpression='SET #org_id = :org_id',
        ExpressionAttributeNames={'#org_id': 'org_id'},
        ExpressionAttributeValues={
            ':org_id': test_company_org_id
        }
    )


# Queries

def get_organisation():
    table = dynamodb.Table('dynamo-test')
    response = table.get_item(              # we use get because we expect a single result
        Key={
            'PK': 'ORG#0eb258f8-5d2c-425a-972a-acfb6c808fba',
            'SK': '#METADATA#0eb258f8-5d2c-425a-972a-acfb6c808fba'
        }
    )
    item = response['Item']
    print(item)


def get_all_projects_of_ABC_company():
    table = dynamodb.Table('dynamo-test')
    response = table.query(
        KeyConditionExpression=Key('PK').eq(
            'ORG#0eb258f8-5d2c-425a-972a-acfb6c808fba') & Key('SK').begins_with('PRO#')
    )
    items = response['Items']
    pprint.pprint(items)


def main():
    assign_employee_to_project()


if __name__ == "__main__":
    main()
