import boto3
from botocore.exceptions import ClientError

from env import *

resource = boto3.resource('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)



server = resource.Instance('i-72827591')
print server.terminate()
"""
"""
