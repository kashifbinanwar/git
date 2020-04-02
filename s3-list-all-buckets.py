import boto3
import time

s3 = boto3.resource('s3')
prog_exec_time = time.asctime( time.localtime(time.time()) )

print('This program is executed at : ', prog_exec_time)
print('-'*100)
for bucket in s3.buckets.all():
    print('BUCKET NAME: ',bucket.name)
print('-'*100)