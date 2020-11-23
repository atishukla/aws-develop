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
            'name': 'Project X',
            'project_id': project_id
        }
    )


def main():
    create_project()


if __name__ == "__main__":
    main()
