#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('producer','password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('crisalex-X555YI',5672,'/',credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1]
if sys.argv[1] == "General" or sys.argv[1] == ".Consumidor1" or sys.argv[1] == ".Consumidor2":
	message = ' '.join(sys.argv[2:])
	channel.basic_publish(
    	exchange='topic_logs', routing_key=routing_key, body=message)
	print(" [x] Enviado %r:%r" % (routing_key, message))
else:
	print("Mensaje no enviado")
connection.close()
