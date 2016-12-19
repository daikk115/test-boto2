import boto3
from botocore.exceptions import ClientError

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

results = client.create_internet_gateway()
print results

"""
{u'InternetGateway': {u'InternetGatewayId': 'igw-6198c1a5', u'Attachments': []}, 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': 'req-84ddf312-2515-46cd-b9a6-46cce9679899', 'HTTPHeaders': {'date': 'Mon, 19 Dec 2016 18:54:26 GMT', 'content-length': '298', 'content-type': 'text/xml'}}}

"""
