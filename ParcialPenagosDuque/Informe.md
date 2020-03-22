# Parcial 1: Sistemas Distribuido

-  Camilo Penagos
-  Cristian Duque

## Arquitectura

-  Un productor de mensajes
-  Un broker de RabbitMQ
-  Dos consumidores de mensajes
-  El primer consumidor recibirá los mensajes de la cola "Estudiantes"
-  El segundo consumidor recibirá los mensajes de la cola "Profesores"
-  Ambos consumidores recibirán los mensajes enviados al grupo "General"

<img src ="img/arqui.JPG" height="300" >

## Procedimiento

Para cumplir con el objetivo del ejercicio parcial, es necesario montar un sistema de arquitectura distribuida que consiste en:

**Un Serivodor Broker:** Corresponde a la maquina fisica host ubuntu con la dirección IP 192.168.0.14

**Un Productor de mensajes:** Corresponde a una maquina virtual guest Lubuntu con la dirección IP 192.168.0.20

**Un Consumidor 01:** Corresponde a una maquina virtual guest Lubuntu con la dirección IP 192.168.0.24

**Un Consumidor 02:** Corresponde a una maquina virtual guest Lubuntu con la dirección IP 192.168.0.26  



### Broker

Primero, ingresamos como usuario root con el comando sudo su. Luego continuamos con los siguientes comandos:

`apt-get update`

`apt-get install erlang`
Erlang contiene es una dependencia para rabbitmq y permite tener un entorno de ejecucción.

`apt-get install rabbitmq-server`

Intalar el servidor de rabbitmq

`systemctl enable rabbitmq-server`

Habilitar el servicio de rabbitmq

`systemctl start rabbitmq-server`

Iniciar el servicio de rabbitmq

`systemctl status rabbitmq-server`

Con este comando se verifica que efectivamente el servicio de rabbitmq se encuentra habilitado y corriendo, como se observa en la imagen.

<img src ="img/brokerruning.JPG" height="155" >

Por ultimo se verifica que el servicio ha sido instalado en localhost y puede ser accesible por la interfaz web de administración usando el puerto 15672

<img src ="img/broker.JPG" height="140" >


### Productor
### Consumidores

## Funcionamiento - Validación

## Problemas
