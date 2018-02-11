#!/usr/bin/env python3

import boto3
import datetime
import time


sqs = boto3.resource('sqs')

# Get the current queue
queue = sqs.get_queue_by_name(QueueName='test')


# Create a new message
msg_body="world"
msg_attr={
    'Author': {
        'StringValue': 'jingwangian',
        'DataType': 'String'
	},
	'Date':{
		'StringValue': datetime.date.today().isoformat(),
		'DataType':'String'
	}
}

msg_body='http://url/a/b/c/task-{}'

for i in range(11):
	msg = msg_body.format(i)
	response = queue.send_message(MessageBody=msg,MessageAttributes=msg_attr)
	print("Send the msg [{}]".format(msg))
	time.sleep(2)

# The response is NOT a resource, but gives you a message ID and MD5
# print(response.get('MessageId'))
# print(response.get('MD5OfMessageBody'))

