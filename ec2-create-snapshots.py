# creates snapshot of all volumes attached with an instance & create tags automatically

import boto3
from datetime import datetime, timedelta


previous_snapshot = datetime.today() - timedelta(minutes=10)

print(previous_snapshot)
creation_time=datetime.strftime(datetime.now(), '%d-%m-%Y %T')

ec2_c = boto3.client('ec2')

InstanceId = 'i-018a3759441b047c9'      # change value of different instance

response = ec2_c.create_snapshots(
    InstanceSpecification={'InstanceId': InstanceId,'ExcludeBootVolume': False},
    TagSpecifications=[{'ResourceType':'snapshot',
                        'Tags': [{'Key': 'creation_time','Value': creation_time}]
    }
        ])