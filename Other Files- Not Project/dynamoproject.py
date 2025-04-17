import boto3

TABLE_NAME = "City"

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)