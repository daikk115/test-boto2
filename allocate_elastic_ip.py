import boto3
from botocore.exceptions import ClientError

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

try:
     output = client.allocate_address(Domain='vpc')
     print type(output)
except ClientError as exc:
    print type(exc)
