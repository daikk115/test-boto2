import boto3
client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')


for i in range(1,10) :
    print i
    cidr = "12.13.{}.0/24". format(i)
    output = client.create_vpc(
        CidrBlock=cidr,
    	InstanceTenancy='default'
    )
    output = client.create_subnet(
        VpcId=output.get('Vpc').get('VpcId'),
        CidrBlock=cidr
    )

"""

"""
