import boto3
import uuid

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
    response = table.get_item(
        Key={
            'PK': 'ORG#0eb258f8-5d2c-425a-972a-acfb6c808fba',
            'SK': '#METADATA#0eb258f8-5d2c-425a-972a-acfb6c808fba'
        }
    )
    item = response['Item']
    print(item)


def main():
    get_organisation()


if __name__ == "__main__":
    main()
