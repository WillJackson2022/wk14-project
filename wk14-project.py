import boto3

# replace the keys below

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='AKIAVO3PXH44OC4GR6X2',
    aws_secret_access_key='JcUHh3Uvo+5JU4Of9balF24Op6BlmxX5JiHihxGB',
    )
table = dynamodb.create_table(
    TableName='Rap_Top_10',
    KeySchema=[
        {
            'AttributeName': 'artist',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'album_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'artist',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'album_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
   }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)