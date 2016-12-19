from env import *
import boto3

from env import *

client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)


cidr = "12.13.15.0/24"
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
{u'Subnet': {u'VpcId': 'vpc-3dc292f8', u'CidrBlock': '12.13.15.0/24', u'DefaultForAz': False, u'State': 'available', u'MapPublicIpOnLaunch': False, u'SubnetId': 'subnet-b43289e0', u'AvailableIpAddressCount': 252}, 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': 'req-1b4b5dac-0923-4d0c-9003-fd8e23433220', 'HTTPHeaders': {'date': 'Mon, 19 Dec 2016 19:03:14 GMT', 'content-length': '479', 'content-type': 'text/xml'}}}

root@bkcloud:/home/bkcloud# openstack router list
+--------------------------------------+----------------+--------+-------+-------------+-------+----------------------------------+
| ID                                   | Name           | Status | State | Distributed | HA    | Project                          |
+--------------------------------------+----------------+--------+-------+-------------+-------+----------------------------------+
| 3b0a184f-3f7b-481c-b87c-a673a66f557c | vpc-3dc292f8   | ACTIVE | UP    | False       | False | c68acedcbd144f2e83764ac4fb6b0bf9 |
| 50c67d5e-8b9b-4e64-814b-2cb73eb26235 | router1        | ACTIVE | UP    | False       | False | f82e54b8893c419b9039783a43c5f8c8 |
| ce1e7244-bffb-4a65-beb6-98219c3ce081 | private_router | ACTIVE | UP    | False       | False | 91eedf84810e46918e5041719f5424d1 |
| cf7c2835-4356-4147-84f7-19cf026a5a46 | vpc-39283a02   | ACTIVE | UP    | False       | False | c68acedcbd144f2e83764ac4fb6b0bf9 |
+--------------------------------------+----------------+--------+-------+-------------+-------+----------------------------------+
"""
