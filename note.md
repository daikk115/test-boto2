- DescribeAccountAttributes
In ec2 api only show max instances, but in bellow link, aws said:

https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAccountAttributes.html

Describes attributes of your AWS account. The following are the supported account attributes:

supported-platforms: Indicates whether your account can launch instances into EC2-Classic and EC2-VPC, or only into EC2-VPC.
default-vpc: The ID of the default VPC for your account, or none.
max-instances: The maximum number of On-Demand instances that you can run.
vpc-max-security-groups-per-interface: The maximum number of security groups that you can assign to a network interface.
max-elastic-ips: The maximum number of Elastic IP addresses that you can allocate for use with EC2-Classic.
vpc-max-elastic-ips: The maximum number of Elastic IP addresses that you can allocate for use with EC2-VPC.

