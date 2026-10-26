import boto3
from datetime import datetime
import uuid
import os
import json

ORDERS_TABLE = os.environ["ORDERS_TABLE"]
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(ORDERS_TABLE)

def lambda_handler(event, context):
    # Ensure order_id is defined before it is used
    order_id = f"order-{uuid.uuid4()}"
    
    # Safely extract the verification field
    if "body" in event:
        body = json.loads(event["body"]) if isinstance(event["body"], str) else event["body"]
        verification = body.get("verification")
    else:
        verification = event.get("verification")

    # Write the item to DynamoDB
    table.put_item(
        Item={
    "verification": "20261026115138",
            "orderId": order_id,
            "userId": "mock-user",
            "productId": "mock-product",
            "quantity": 1,
            "status": "CREATED",
            "createdAt": datetime.utcnow().isoformat()
        }
    )

    return {
        "orderId": order_id,
        "status": "CREATED",
        "verification": verification
    }