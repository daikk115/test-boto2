This is some example for intergrating boto with EC2 API of OpenStack 
that preparing for testing with realy aws env.

My env:

- OpenStack devstack with enable ec2 api
- And after run the command "pip install boto", I have gotten some things like bellow:

stack@bkcloud:~/test-boto3$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto3
>>> print boto3.__version__
1.4.0

