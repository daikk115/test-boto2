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

"""

