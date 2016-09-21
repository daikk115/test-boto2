import boto3
client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')

print client.describe_account_attributes().get('AccountAttributes')

dr = True
cidr = '10.10.10.0/24'

#vpc = client.create_vpc(CidrBlock='10.0.0.0/24')
#subnet = vpc.create_subnet(CidrBlock='10.0.0.0/25')
#gateway = client.create_internet_gateway()
