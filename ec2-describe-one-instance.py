
import boto3
import sys

''' returns status of instance whose id is passed as argument '''

ec2 = boto3.client('ec2')
s = ' '
instanceid = sys.argv[1]

response = ec2.describe_instances(InstanceIds=[instanceid])['Reservations']
print('-' * 150)
print('InstanceID', s*8, 'State', s*1, 'InstanceType', 'VpcId', s*15, 'PrivateIpAddress', 'SubnetId',s*15, 'SecurityGroups',s*7,'AvailabilityZone', 'PublicIpAddress')
print('-' * 150)

for instance in response:
    for att in instance['Instances']:
        if att['State']['Name'] == 'running':
            print(att['InstanceId'], att['State']['Name'], att['InstanceType'], s*3, att['VpcId'], att['PrivateIpAddress'], s*4, att['SubnetId'],att['SecurityGroups'][0]['GroupId'], s*1,att['Placement']['AvailabilityZone'], s, att['PublicIpAddress'])
        else:
            print(att['InstanceId'], att['State']['Name'], att['InstanceType'], s*3, att['VpcId'],s*8, att['PrivateIpAddress'], s*4, att['SubnetId'],att['SecurityGroups'][0]['GroupId'], s*10,att['Placement']['AvailabilityZone'], s, 'NULL')

print('\n')