import boto3
client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')

dr = True
cidr = '10.10.10.0/24'

output = client.create_subnet(
    VpcId='vpc-5eed72c5',
    CidrBlock=cidr)

print output

"""
Respone

{u'Subnet': {u'VpcId': 'vpc-5eed72c5', u'CidrBlock': '10.10.10.0/24', u'DefaultForAz': False, u'State': 'available', u'MapPublicIpOnLaunch': False, u'SubnetId': 'subnet-9dcb6b38', u'AvailableIpAddressCount': 252}, 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'req-261a0331-1d6a-4bfc-92b1-5de9178cdf85', 'HTTPHeaders': {'date': 'Tue, 13 Sep 2016 10:25:20 GMT', 'content-length': '479', 'content-type': 'text/xml'}}}


After create network, we can see:

stack@bkcloud:~/devstack$ openstack network list
+--------------------------------------+-----------------+----------------------------------------------------------------------------+
| ID                                   | Name            | Subnets                                                                    |
+--------------------------------------+-----------------+----------------------------------------------------------------------------+
| 2bd56ece-39a5-4702-b99a-693a9f7354eb | private         | ed6978f4-41d1-4dcb-85fb-c34f03adac04, f196a012-366d-435f-a4f5-142ba49e545b |
| 708b8b9a-d7b3-4e89-b032-cccb7c02ea31 | public          | 04020d09-eb21-4d86-bc35-a7bbb676730e, f1a234b1-ef03-4553-8659-4ae0f5dce5ef |
| 7fdb8045-00d5-4024-a6e1-50637a47c4bd | private         | ef0b84c8-edca-4fb3-b943-e80e6a5bc711                                       |
| 168da6fa-5473-4e99-aee4-31cb25ff03ff | subnet-9dcb6b38 | 7b67b3b8-88d2-4169-8162-03db4ef5a8a6                                       |
+--------------------------------------+-----------------+----------------------------------------------------------------------------+
stack@bkcloud:~/devstack$ neutron network-list
Unknown command [u'network-list']
stack@bkcloud:~/devstack$ neutron net-list
+--------------------------------------+-----------------+----------------------------------------------------------+
| id                                   | name            | subnets                                                  |
+--------------------------------------+-----------------+----------------------------------------------------------+
| 2bd56ece-39a5-4702-b99a-693a9f7354eb | private         | f196a012-366d-435f-a4f5-142ba49e545b fd9b:7c0a:ed6e::/64 |
|                                      |                 | ed6978f4-41d1-4dcb-85fb-c34f03adac04 100.0.0.0/24        |
| 708b8b9a-d7b3-4e89-b032-cccb7c02ea31 | public          | 04020d09-eb21-4d86-bc35-a7bbb676730e 192.168.122.0/24    |
|                                      |                 | f1a234b1-ef03-4553-8659-4ae0f5dce5ef 2001:db8::/64       |
| 7fdb8045-00d5-4024-a6e1-50637a47c4bd | private         | ef0b84c8-edca-4fb3-b943-e80e6a5bc711 10.0.0.0/24         |
| 168da6fa-5473-4e99-aee4-31cb25ff03ff | subnet-9dcb6b38 | 7b67b3b8-88d2-4169-8162-03db4ef5a8a6 10.10.10.0/24       |

"""
