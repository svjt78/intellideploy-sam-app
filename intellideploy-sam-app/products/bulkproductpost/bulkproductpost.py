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
    data = []
	data=json.loads(event['body'])

	try:
        do ix in range(len(data)):

		  table.put_item(
	         Item={
	            'PRODUCT_ID': data[ix]["productid"],
	            'LOCAL_ID': data[ix]["id"],
				'ITEM_ID': ts,
	            'NAME': data[ix]["name"],
	            'TYPE': data[ix]["type"],
	            'SLUG': data[ix]["slug"],
	            'DESCRIPTION': data[ix]["description"],
	            'COVERAGE_LIMIT': data[ix]["coverage_limit"],
	            'RATE': data[ix]["price_per_1000_units"],
	            'CREATOR': data[ix]["creator"],
	            'CREATE_DATE': data[ix]["product_date"],
	            'PHOTO': data[ix]["photo"],
	            'CONNECTION': data[ix]["backend_SOR_connection"],
				'RECORD_STATUS': data[ix]["record_status"],
				'COMMIT_INDICATOR': data[ix]["commit_indicator"],
				'RESPONSE': data[ix]["response"],
                'BULK_UPLOAD_INDICATOR': data[ix]["bulk_upload_indicator"]

	           }
	    )


	except Exception as e:
	        print(e)
	        print('Error in reading data from intellidataTable')
	        raise e
