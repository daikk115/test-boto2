import boto3
client = boto3.client('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

subnets = client.describe_subnets().get('Subnets')
for subnet in subnets:
    print "deleted"
    print client.delete_subnet(SubnetId=subnet['SubnetId'])

