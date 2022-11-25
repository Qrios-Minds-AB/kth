import json



def lambda_handler(event, context):
    for record in event['Records']:
        recordDic = json.loads(record['Sns']['Message'])
        print(recordDic)
        # Process Events based on type
        if 'customerId' in recordDic:
            print('Enriching cutomer with id', recordDic['customerId'])
        if 'orderId' in recordDic:
            print('Enriching order with id', recordDic['orderId'])
        print('sending to data platform')