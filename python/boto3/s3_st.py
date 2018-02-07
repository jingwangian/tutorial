#!/usr/bin/env python3


import boto3

s3 = boto3.resource('s3')


# create a bucket object
bucket_name='ub1.flight.test'
bucket = s3.Bucket(bucket_name)


# go throught the objects in one bucket
num=10
for key in bucket.objects.all():
	print(key)
	print(type(key))
	num -=1
	if num==0:
		break

#storing data from a file data
s3.Object(bucket_name, 'why.txt').put(Body=open('/db2/github/tutorial/why.txt', 'rb'))