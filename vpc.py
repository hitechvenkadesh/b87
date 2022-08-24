import boto3
import sys

region=sys.argv[1]
access_key=sys.argv[2]
secret_key=sys.argv[3]

client = boto3.client('ec2',
	region_name = region,
	aws_access_key_id = access_key, 
	aws_secret_access_key = secret_key)

#Create VPC
myvpc = client.create_vpc(
	CidrBlock='10.10.0.0/16',
	TagSpecifications=[
        {
            'ResourceType': 'vpc',
			'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'htvpc'
                }
            ]
        }
    ]
)
print('VPC-ID:',myvpc['Vpc']['VpcId'])

#Create Subnet
mysubnet = client.create_subnet(
	AvailabilityZone='us-east-2a',
	CidrBlock='10.10.1.0/24',
	VpcId=myvpc['Vpc']['VpcId'],
	TagSpecifications=[
        {
            'ResourceType':'subnet',
			'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'htsubnet'
                }
            ]
        }
    ]
)
print('SUBNET-ID:',mysubnet['Subnet']['SubnetId'])

#Create RouteTable
myroutetable = client.create_route_table(
	VpcId=myvpc['Vpc']['VpcId'],
	TagSpecifications=[
        {
            'ResourceType':'route-table',
			'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'htrt'
                }
            ]
        }
    ]
)
print('RouteTable-ID:',myroutetable['RouteTable']['RouteTableId'])

#Create IGW
myigw = client.create_internet_gateway(
	TagSpecifications=[
        {
            'ResourceType':'internet-gateway',
			'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'htigw'
                }
            ]
        },
    ]
)
print('IGW-ID:',myigw['InternetGateway']['InternetGatewayId'])

attach = client.attach_internet_gateway(
    InternetGatewayId=myigw['InternetGateway']['InternetGatewayId'],
    VpcId=myvpc['Vpc']['VpcId']
)

assoc = client.associate_route_table(
	RouteTableId=myroutetable['RouteTable']['RouteTableId'],
    SubnetId=mysubnet['Subnet']['SubnetId']
)
print("Subnet-Associated")

route = client.create_route(
	RouteTableId=myroutetable['RouteTable']['RouteTableId'],
	DestinationCidrBlock='0.0.0.0/0',
	GatewayId=myigw['InternetGateway']['InternetGatewayId']
)
print("RouteEntryDone")
