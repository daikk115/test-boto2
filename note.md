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

- Can add multi networks with same cidr??

This is result when I run more than one create function.

stack@bkcloud:~/test-boto3$ neutron net-list
+--------------------------------------+-----------------+----------------------------------------------------------+
| id                                   | name            | subnets                                                  |
+--------------------------------------+-----------------+----------------------------------------------------------+
| 7fdb8045-00d5-4024-a6e1-50637a47c4bd | private         | ef0b84c8-edca-4fb3-b943-e80e6a5bc711 10.0.0.0/24         |
| 43badc7c-2e54-4b3f-b8b9-bcdb107d6624 | subnet-95553025 | 5d82a1d7-bf7d-4342-b8cf-834edf98347b 12.13.1.0/24        |
| ac04fff5-39e2-43d0-ac45-c3f7a36fb446 | subnet-222d74ce | 768c0d31-f690-4e65-9d9f-aa0ae3b90817 12.13.1.0/24        |
| 4bcef6a8-7063-4e04-9884-8a8f05508b82 | subnet-498b6e3c | 6fd771ce-70a9-497d-806c-9b386efe8099 12.13.1.0/24        |
| 56ec977b-22d3-4ddd-9de6-23b7cda348f1 | subnet-91cf8128 | cb6d0a57-29d5-4792-a821-6dac606f690f 12.13.1.0/24        |
| 1a5990ea-ff1f-4fe0-8d8d-83fb96c54f20 | subnet-917315d5 | a4027259-9e8d-4892-b1fb-e072d1c61a99 12.13.1.0/24        |
| 708b8b9a-d7b3-4e89-b032-cccb7c02ea31 | public          | 04020d09-eb21-4d86-bc35-a7bbb676730e 192.168.122.0/24    |
|                                      |                 | f1a234b1-ef03-4553-8659-4ae0f5dce5ef 2001:db8::/64       |
| 26878b1a-bbdb-478b-8c54-71933adf05bc | subnet-914c0bd2 | d2d96849-6a7e-47ba-ab6c-80e623da3877 12.13.1.0/24        |
| 2bd56ece-39a5-4702-b99a-693a9f7354eb | private         | ed6978f4-41d1-4dcb-85fb-c34f03adac04 100.0.0.0/24        |
|                                      |                 | f196a012-366d-435f-a4f5-142ba49e545b fd9b:7c0a:ed6e::/64 |
+--------------------------------------+-----------------+----------------------------------------------------------+

