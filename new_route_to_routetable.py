import boto3
from botocore.exceptions import ClientError

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

results = client.create_route(
		RouteTableId='rtb-1a3bc88c',
		GatewayId='igw-a9c7131a',
		DestinationCidrBlock='0.0.0.0/0'
)

print results

"""

Before and After add route 0.0.0.0/0 to routetable

bkcloud@bkcloud:~$ sudo ip netns e qdhcp-503c4478-8a9a-4f19-a292-f451bb74c905 ip r                                                              12.13.16.0/24 dev tap38c38d5b-91  proto kernel  scope link  src 12.13.16.2 
bkcloud@bkcloud:~$ sudo ip netns e qdhcp-503c4478-8a9a-4f19-a292-f451bb74c905 ip r
default via 12.13.16.1 dev tap38c38d5b-91 
12.13.16.0/24 dev tap38c38d5b-91  proto kernel  scope link  src 12.13.16.2 

Now, inside network can connect to internet
"""
