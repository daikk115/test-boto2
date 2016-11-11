import boto3
from botocore.exceptions import ClientError

client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')

try:
     results = client.describe_addresses().get('Addresses')
     return_format = []
     for ip in results:
         return_format.append(ip.get('PublicIp'))
     print return_format
except ClientError as exc:
    print type(exc)

"""
{u'Addresses': [{u'PublicIp': '192.168.122.224', u'Domain': 'vpc', u'AllocationId': 'eipalloc-8f665a3d'}, {u'PublicIp': '192.168.122.225', u'Domain': 'vpc', u'AllocationId': 'eipalloc-65972269'}, {u'PublicIp': '192.168.122.222', u'Domain': 'vpc', u'AllocationId': 'eipalloc-1267a078'}, {u'PublicIp': '192.168.122.223', u'Domain': 'vpc', u'AllocationId': 'eipalloc-2dcd562c'}, {u'PublicIp': '192.168.122.227', u'Domain': 'vpc', u'AllocationId': 'eipalloc-0018cc6e'}, {u'PublicIp': '192.168.122.226', u'Domain': 'vpc', u'AllocationId': 'eipalloc-79c096b2'}], 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'req-30d6aad8-7bac-41b8-8d14-be054559cf1d', 'HTTPHeaders': {'date': 'Thu, 10 Nov 2016 20:48:25 GMT', 'content-length': '1083', 'content-type': 'text/xml'}}}
"""
