import boto3
from botocore.exceptions import ClientError

from env import *

client = boto3.resource('ec2',
                aws_access_key_id=access,
                aws_secret_access_key=secret,
                region_name='RegionOne',
                endpoint_url=endpoint)

IamInstanceProfile={
        'Arn': '',
        'Name': 'Daidv'
}
results = client.create_instances(ImageId='ami-1e839cd7',
    			MinCount=1, MaxCount=1 ,
    			InstanceType='m1.tiny', SubnetId='subnet-8ba22194')
print results

"""
"""
