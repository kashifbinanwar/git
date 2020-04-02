import boto3

ec2_c = boto3.client('ec2')

s = " "
c = 15

response = ec2_c.describe_addresses()

print ('-' *100)
print('PublicIp', s*8, 'InstanceId',s*8, 'PrivateIpAddress' )
print ('-' *100)


for addr in response['Addresses']:
    if addr.get('InstanceId') != None:
        print(addr.get('PublicIp'), s*int(c-len(addr.get('PublicIp'))),
            addr.get('InstanceId'), s*int(c-len(addr.get('InstanceId'))), addr.get('PrivateIpAddress'))

for addr in response['Addresses']:    
    if addr.get('InstanceId') == None:
        print(addr.get('PublicIp'), s*int(c-len(addr.get('PublicIp'))),
            addr.get('InstanceId'), s*c, addr.get('PrivateIpAddress'))
print('\n')
