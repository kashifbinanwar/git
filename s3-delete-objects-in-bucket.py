import boto3

''' this program delete objects related to a specific key_prefix'''

s3 = boto3.client('s3')

key_prefix ='AWSLogs/162483680204/CloudTrail-Digest/ap-southeast-2/'
key_prefix =input ("Please input the key prefix e.g. 'AWSLogs/162483680204/CloudTrail-Digest/ap-southeast-2/' : ")

bucket = 'bucketfornormalwork.1984.com'

response = s3.list_objects(Bucket= bucket)

for object in response['Contents']:
    key = object['Key']
    if key_prefix not in key: continue
    else:
        print('Deleting: ', key)
        s3.delete_object(Bucket=bucket,Key= key)
    
        