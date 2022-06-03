import boto3

s3 = boto3.resource('s3')

print("Example S3 buckets")
for bucket in s3.buckets.all():
    print(bucket.name)

print("Example Describe EC2")

ec2 = boto3.resource('ec2')
instance = ec2.Instance('id')
