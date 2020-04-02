# this script prints all the snapshots in account, associated volumes, snapshot_creation date and snapshot tags in table form.

import boto3
from datetime import datetime, timedelta,timezone

ec2_r = boto3.resource('ec2')
s = ' '
d=7
e=10

current_time = datetime.now(timezone.utc) # this value is in UTC time
        
print ('-' * 150)
print ('Volume_id',s*11,'Snapshot_id', s*e, 'Creation_time(UTC)',s*3,'Size(GB)', 'Status', s*3,'Age(days)', 'Tags' )
print ('-' * 150)

for snapshot in ec2_r.snapshots.filter(OwnerIds=['162483680204']):  # change owner id for different account
    
    creation_time = snapshot.start_time
    age = current_time - creation_time
    creation_time_str = datetime.strftime(snapshot.start_time, '%d-%m-%Y %T')
    
    creation_time=datetime.strftime(datetime.now(), '%d-%m-%Y %T')
    print (snapshot.volume_id,snapshot.id, creation_time_str, s*3,snapshot.volume_size,
           s*int(5 -len(str(snapshot.volume_size))),snapshot.state, s*4,age.days, s*5, snapshot.tags)
    