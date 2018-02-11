#!/usr/bin/env python3

import boto3
import time

sqs = boto3.resource('sqs')

# Get the current queue
queue = sqs.get_queue_by_name(QueueName='test')

while(1):
	try:
		for message in queue.receive_messages():
		    author_text = ''
		    if message.message_attributes is not None:
		        author_name = message.message_attributes.get('Author').get('StringValue')
		        if author_name:
		            author_text = ' ({0})'.format(author_name)

		    # Print out the body and author (if set)
		    print('Received the msg [{0}]!{1}'.format(message.body, author_text))

		    # Let the queue know that the message is processed
		    message.delete()

		    time.sleep(1)
	except KeyboardInterrupt:
		print('Exit the process')
		break
