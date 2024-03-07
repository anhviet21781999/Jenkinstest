'''
VPC
+ scalable and highly configurable AWS service
Provides networking functionality
A customizable logically isolated section of AWS cloud
Including selection of oyour own IP address range, create of subnets, and configuration of route tables and network gateways
Into whcih you can launch AWS resource

'''


#create VPC
import boto3
import time
ec2 = boto3.client('ec2')

vpc_name = 'vpc-hol'
vpc_response = ec2.create_vpc(CidrBlock= '10.0.0.0/16')
vpc_id = vpc_response['Vpc']['VpcId']


time.sleep(5)
ec2.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': vpc_name}])
print(f"VPC {vpc_name} with id {vpc_id} has been created")