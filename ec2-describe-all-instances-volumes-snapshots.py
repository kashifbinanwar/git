
# this script prints all instances in the account, volumes attached with each instances and snapshots of each volume 

import boto3


s = ' '
ec2 = boto3.resource('ec2')
print('\n')
for instance in ec2.instances.all():
     print('InstanceID: ', instance.id)
     for volume in instance.volumes.all():
          print(s*2,'VolumeID: ', volume.id, '| VolumeSize: ', volume.size)
          for snapshot in volume.snapshots.all():
               print(s*4, 'SanpshotID: ',snapshot.id, snapshot.start_time, snapshot.state)
             
     print('\n')