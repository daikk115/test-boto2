import boto3
from botocore.exceptions import ClientError

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

results = client.describe_internet_gateways(
	Filters=[
        {
            'Name': 'attachment.vpc-id',
            'Values': [
                'vpc-839cc730',
            ]
        },
    	]
)
print results.get('InternetGateways')[0].get('InternetGatewayId')

"""
id of gateway which  attach to vpc
"""
