from env import *
import boto3

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

output = client.describe_vpcs(VpcIds=['vpc-39283a02'])

print output

"""
Respone

{u'Vpcs': [{u'State': 'available', u'VpcId': 'vpc-5eed72c5', u'CidrBlock': '10.10.10.0/24', u'IsDefault': False, u'DhcpOptionsId': 'default'}, {u'State': 'available', u'VpcId': 'vpc-c83b53c6', u'CidrBlock': '10.10.10.0/24', u'IsDefault': False, u'DhcpOptionsId': 'default'}], 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'req-6a42cc89-50f9-4fa2-9bd5-026df54b7541', 'HTTPHeaders': {'date': 'Tue, 13 Sep 2016 10:56:52 GMT', 'content-length': '607', 'content-type': 'text/xml'}}}

"""
