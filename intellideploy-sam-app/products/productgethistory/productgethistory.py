import json
from decimal import *
import boto3
from boto3.dynamodb.conditions import Key, Attr

#always start with the lambda_handler
def lambda_handler(event, context):

    # make the connection to dynamodb
    dynamodb = boto3.resource('dynamodb')

    # select the table
    table = dynamodb.Table('intellidataTable')

    ident = event['queryStringParameters']['ident']

    try:
         #response = table.get_item(Key={'LOCAL_ID': ident, 'ITEM_ID': ts})
         response = table.query(
            KeyConditionExpression=Key('PRODUCT_ID').eq(ident), ScanIndexForward=False
         )

         data = response['Items']

         return {
                    'statusCode': 200,
                    'headers': {'Content-Type': 'application/json'},
                    'body': json.dumps(data, cls=CustomJsonEncoder)
                }

    except Exception as e:
        print(e)
        print('Error in reading data from intellidataTable')
        raise e


class CustomJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(CustomJsonEncoder, self).default(obj)
