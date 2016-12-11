import boto3
from botocore.exceptions import ClientError

client = boto3.resource('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

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
