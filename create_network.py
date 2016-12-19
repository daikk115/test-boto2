from env import *
import boto3

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)


cidr = "12.13.14.0/24"
output = client.create_vpc(
    CidrBlock=cidr,
	InstanceTenancy='default'
)
output = client.create_subnet(
    VpcId=output.get('Vpc').get('VpcId'),
    CidrBlock=cidr
)
print output

"""

"""
