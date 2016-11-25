import boto3
from botocore.exceptions import ClientError

client = boto3.resource('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')

IamInstanceProfile={
        'Arn': '',
        'Name': 'Daidv'
}
results = client.create_instances(ImageId='ami-2624df94',
    			MinCount=1, MaxCount=1 ,
    			InstanceType='m1.tiny', SubnetId='subnet-ac04352a')
print results

"""
"""
