import boto3
from datetime import datetime

ec2 = boto3.client('ec2')
s = ' '

check_time = datetime.strftime(datetime.now(), '%d-%m-%Y %T')

response = ec2.describe_instances()['Reservations']

print('-' * 200)
print('CheckTime', s*9, 'InstanceID', s*8, 'State', s*1, 'InstanceType', 'VpcId', s*17, 'PrivateIpAddress', 'SubnetId',s*15, 'SecurityGroups',s,'AvailabilityZone', 'PublicIpAddress')
print('-' * 200)

for instance in response:
    for att in instance['Instances']:
        print(check_time, att['InstanceId'], att.get('State')['Name'], att.get('InstanceType'), s*3, att.get('VpcId'), s*10, att.get('PrivateIpAddress'), s*4, att.get('SubnetId'),att.get('SecurityGroups')[0]['GroupId'], s*4, att.get('Placement')['AvailabilityZone'], s, att.get('PublicIpAddress'))
       
print('\n')