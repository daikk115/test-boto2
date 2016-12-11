import boto3

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

vpcs = client.describe_vpcs().get('Vpcs')
for vpc in vpcs:
    print "deleted"
    print client.delete_vpc(VpcId=vpc['VpcId'])

