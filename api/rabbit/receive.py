#!/usr/bin/env python
import pika, sys, os

def main():
    credentials = pika.PlainCredentials('sensors', 'sensors')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.121', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='sensor_readings')

    def callback(ch, method, properties, body):
        print(f' [x] Received {body}')

    channel.basic_consume(queue='sensor_readings', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)