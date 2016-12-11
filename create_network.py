import boto3

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)


for i in range(1,10) :
    print i
    cidr = "12.13.{}.0/24". format(i)
    output = client.create_vpc(
        CidrBlock=cidr,
    	InstanceTenancy='default'
    )
    output = client.create_subnet(
        VpcId=output.get('Vpc').get('VpcId'),
        CidrBlock=cidr
    )

"""

"""
