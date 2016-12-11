import boto3

from env import *

client = boto3.client('ec2',
		aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
		endpoint_url=endpoint)

print client.describe_account_attributes().get('AccountAttributes')

dr = True
cidr = '10.10.10.0/24'

#vpc = client.create_vpc(CidrBlock='10.0.0.0/24')
#subnet = vpc.create_subnet(CidrBlock='10.0.0.0/25')
#gateway = client.create_internet_gateway()
