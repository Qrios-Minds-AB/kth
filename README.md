# Overview

An AWS solution that allow differnt applications stream data from Lambda Functions to SNS Topic.
The repo structure:
- customers-app: contains a simple application that has Lambda fucntion and API Gateway to process customers data.
- orders-app: contains a simple application that has Lambda fucntion and API Gateway to process orders data.
- data-processing: contains the SNS topic, DLQ and Lambda that subscribes to SNS topic to process the data.

The code sample are in python 3.8 and there are no external packages except boto3.
All AWS workloads are manage using SAM template, Check SAM documenation to build, test locally and deploy to AWS account. [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html)

The Workloads are based on Serverless and trying it on AWS will not require cost beyond the free-tier.

## License

[MIT](https://choosealicense.com/licenses/mit/)