import boto3
client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')

output = client.describe_subnets()

print output

"""
Respone

{u'Subnets': [{u'VpcId': 'vpc-5eed72c5', u'CidrBlock': '10.10.10.0/24', u'DefaultForAz': False, u'State': 'available', u'MapPublicIpOnLaunch': False, u'SubnetId': 'subnet-9dcb6b38', u'AvailableIpAddressCount': 252}], 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'req-c319e7b3-ef93-4c3d-8571-59bcb3216320', 'HTTPHeaders': {'date': 'Tue, 13 Sep 2016 10:57:58 GMT', 'content-length': '528', 'content-type': 'text/xml'}}}

"""
