import boto3
client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')
output = client.allocate_address(Domain='vpc')
print output

"""
{u'PublicIp': '192.168.122.223', u'Domain': 'vpc', u'AllocationId': 'eipalloc-2dcd562c', 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'req-e078e96c-bec4-4365-bf80-d365d9b4cb26', 'HTTPHeaders': {'date': 'Thu, 10 Nov 2016 03:53:28 GMT', 'content-length': '279', 'content-type': 'text/xml'}}}
"""
