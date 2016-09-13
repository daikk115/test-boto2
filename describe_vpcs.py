import boto3
client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')

output = client.describe_vpcs()

print output

"""
Respone

{u'Vpcs': [{u'State': 'available', u'VpcId': 'vpc-5eed72c5', u'CidrBlock': '10.10.10.0/24', u'IsDefault': False, u'DhcpOptionsId': 'default'}, {u'State': 'available', u'VpcId': 'vpc-c83b53c6', u'CidrBlock': '10.10.10.0/24', u'IsDefault': False, u'DhcpOptionsId': 'default'}], 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'req-6a42cc89-50f9-4fa2-9bd5-026df54b7541', 'HTTPHeaders': {'date': 'Tue, 13 Sep 2016 10:56:52 GMT', 'content-length': '607', 'content-type': 'text/xml'}}}

"""
