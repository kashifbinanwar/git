
import boto3


print('-' * 100)
print('This program prints objects of a bucket')
print('-' * 100)

s3 = boto3.resource('s3')

mybucket = input('Please input bucket name without quotes: ')

bucket_names = []

for bucket in s3.buckets.all():
    bucket_names.append(bucket.name)

if mybucket in bucket_names:
    bucket = s3.Bucket(mybucket)
    print('printing object inside of ', bucket.name)
    for obj in bucket.objects.all():
        print(obj.key)