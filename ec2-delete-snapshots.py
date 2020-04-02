# this script deletes any snapshots that is older than 60 days.

import boto3
from datetime import datetime, timedelta,timezone

ec2_r = boto3.resource('ec2')

current_time = datetime.now(timezone.utc)       # this value is in UTC time
snapshot_age = 60                               # number of days from snapshot creation time
owner_id = ['162483680204']                     # AWS Account_id     

for snapshot in ec2_r.snapshots.filter(OwnerIds=owner_id):   # filtering snapshots based on OwnerId        
        creation_time = snapshot.start_time                  # this value is in UTC time
        delta = current_time - creation_time       
       
       # delete any snapshots that were created 60 days ago
       
        if delta.days > snapshot_age:
            
            print('\n')
            print('Deleting Snapshot.......')
            print('snapshot_id: ',snapshot.id)
            print('creation_time:  ', snapshot.start_time)
            print('current_time:  ', datetime.now(timezone.utc))
            print('age(days):  ', delta.days)
            snapshot.delete()
        else:
            print('\n')
            print('Not Deleteing')
            print('snapshot_id: ',snapshot.id)
            print('creation_time:  ', snapshot.start_time)
            print('current_time:  ', datetime.now(timezone.utc))
            print('age(days): '  , delta.days)
            
            
        
    
