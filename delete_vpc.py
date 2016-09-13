import boto3
client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')

output_subnet = client.delete_subnet(SubnetId='subnet-9dcb6b38')
output_vpc = client.delete_vpc(VpcId='vpc-5eed72c5')

print output_subnet
print output_vpc

"""
Respone

{'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'req-ce0ec162-8d2e-449f-a824-ca3fb6665b88', 'HTTPHeaders': {'date': 'Tue, 13 Sep 2016 11:02:45 GMT', 'content-length': '186', 'content-type': 'text/xml'}}}
{'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'req-51ff0526-270e-48bd-bba5-46a84a5ff152', 'HTTPHeaders': {'date': 'Tue, 13 Sep 2016 11:02:46 GMT', 'content-length': '180', 'content-type': 'text/xml'}}}

NOTE: we must delete subnet before we want to delete vpc. 
This is different from OpenStack that I can remove network without deleting subnet
"""
