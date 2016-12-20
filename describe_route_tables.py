import boto3
from botocore.exceptions import ClientError

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

results = client.describe_route_tables()

print results

"""
{'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': 'req-4ece1691-b57f-462a-9a19-b07221534b2d', 'HTTPHeaders': {'date': 'Tue, 20 Dec 2016 09:46:29 GMT', 'content-length': '848', 'content-type': 'text/xml'}}, u'RouteTables': [{u'Associations': [{u'RouteTableAssociationId': 'rtbassoc-839cc730', u'Main': True, u'RouteTableId': 'rtb-1a3bc88c'}], u'RouteTableId': 'rtb-1a3bc88c', u'VpcId': 'vpc-839cc730', u'PropagatingVgws': [], u'Tags': [], u'Routes': [{u'GatewayId': 'local', u'DestinationCidrBlock': '12.13.16.0/24', u'State': 'active', u'Origin': 'CreateRouteTable'}]}]}

"""
