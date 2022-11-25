import json
import uuid
import os;
import boto3;


snsTopicArn = region = os.environ['TargetSnsTopicArn']

snsClient = boto3.client('sns')


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    customerDic = json.loads(event["body"])
    customer = process_customer(customerDic)
    customerId = customer['customerId']
    print(customer)
    print('publishing customer with Id {0} to sns topic.', customerId)
    publish_to_topic(customer)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "customer placed sucessfully.",
            "orderId": customerId
        }),
    }

def process_customer(customer):
    customerId = str(uuid.uuid4())
    customer["customerId"] = customerId
    print(customerId)
    return customer

def publish_to_topic(customer):
    response = snsClient.publish(
        TargetArn = snsTopicArn,
        Message = json.dumps({'default': json.dumps(customer)}),
        MessageStructure = 'json'
    )
    print(response)
