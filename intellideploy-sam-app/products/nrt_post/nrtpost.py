import boto3
import json
import uuid
import csv

def lambda_handler(event, context):

	#recordId = str(uuid.uuid4())

	bucket = client.Bucket('iestandard')
	keyname = Key(bucket)

	dynamodb = boto3.resource('dynamodb')

	table = dynamodb.Table('intellidataTable')

	table.put_item(
        Item={
            #'ItemID': recordId,
            'PRODUCT_LOCALKEY': event["id"],
            PRODUCT_ID': event["productid"],
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

        #	'INCOME': data_dic["income"],
        #	'EXECUTIVE_STATUS': data_dic["executivestatus"]
        }
    )




			#End of code
