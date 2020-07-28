import boto3
import json
import uuid
import csv
import time

def lambda_handler(event, context):

	recordId = str(uuid.uuid4())

#	ts = datetime.datetime.now().timestamp()
	ts = int(round(time.time() * 1000))

	dynamodb = boto3.resource('dynamodb')

	table = dynamodb.Table('intellidataTable')
	event=json.loads(event['body'])

	try:
		table.put_item(
	        Item={
				'LOCAL_ID': event["id"],
				'ITEM_ID': ts,
	            'PRODUCT_ID': event["productid"],
	            'NAME': event["name"],
	            'TYPE': event["type"],
	            'SLUG': event["slug"],
	            'DESCRIPTION': event["description"],
	            'COVERAGE_LIMIT': event["coverage_limit"],
	            'RATE': event["price_per_1000_units"],
	            'CREATOR': event["creator"],
	            'CREATE_DATE': event["product_date"],
	            'PHOTO': event["photo"],
	            'CONNECTION': event["backend_SOR_connection"]

	           }
	    )


	except Exception as e:
	        print(e)
	        print('Error in reading data from intellidataTable')
	        raise e
