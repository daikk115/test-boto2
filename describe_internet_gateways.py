import boto3
from botocore.exceptions import ClientError

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

results = client.describe_internet_gateways()
print results

"""
{u'InternetGateways': [{u'InternetGatewayId': 'igw-6198c1a5', u'Attachments': []}], 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': 'req-40fe0edb-ed79-4296-9dcb-413af96d8973', 'HTTPHeaders': {'date': 'Mon, 19 Dec 2016 18:55:38 GMT', 'content-length': '337', 'content-type': 'text/xml'}}}
"""
