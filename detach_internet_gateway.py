import boto3
from botocore.exceptions import ClientError

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

results = client.detach_internet_gateway(
    InternetGatewayId='igw-6198c1a5',
    VpcId='vpc-624be7bb'
)
print results

"""
"""
