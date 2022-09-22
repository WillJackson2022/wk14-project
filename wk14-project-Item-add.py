import boto3

# replace the keys below

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='AKIAVO3PXH44OC4GR6X2',
    aws_secret_access_key='JcUHh3Uvo+5JU4Of9balF24Op6BlmxX5JiHihxGB',
    )
    
table = dynamodb.Table('Rap_Top_10')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'artist': 'Jayz',
            'album_name': 'Black Album'
            }
    )
    batch.put_item(
        Item={
            'artist': 'Fabolous',
            'album_name': 'Soul Tapes'
            }
    )
    batch.put_item(
        Item={
            'artist': 'Mase',
            'album_name': 'Harlem World'
            }
    )
    batch.put_item(
        Item={
            'artist': 'Biggie',
            'album_name': 'Life After Death'
            }
    )
    batch.put_item(
        Item={
            'artist': 'Nas',
            'album_name': 'King Disease 1 & 2'
            }
    )
    batch.put_item(
        Item={
            'artist': 'Jadakiss',
            'album_name': 'Kiss The Game Goodbye'
            }
    )
    batch.put_item(
        Item={
            'artist': 'Drake',
            'album_name': 'Take Care'
            }
    )
    batch.put_item(
        Item={
            'artist': 'Jayz',
            'album_name': 'Blue Print 1 & 2'
            }
    )
    batch.put_item(
        Item={
            'artist': 'Jayz',
            'album_name': 'MCHG'
            }
    )
    batch.put_item(
        Item={
            'artist': 'Busta Rhymes',
            'album_name': 'Extinction Level Event 1 & 2'
            }
    )
    batch.put_item(
        Item={
            'artist': 'Kendrick Lamar',
            'album_name': 'Good Kid Mad City'
            }
    )


# Wait until the table exists.
#table.wait_until_exists()

# Print out some data about the table.
#print(table.item_count)
print(table.creation_date_time)