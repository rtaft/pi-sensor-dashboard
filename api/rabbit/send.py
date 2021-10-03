#!/usr/bin/env python
import pika
credentials = pika.PlainCredentials('sensors', 'sensors')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.1.121', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='read', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()