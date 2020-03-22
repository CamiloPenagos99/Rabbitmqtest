#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('consumer2','password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('crisalex-X555YI',5672,'/',credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='Grupo 02', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(
   callback, queue=queue_name, no_ack=True)

channel.start_consuming()
