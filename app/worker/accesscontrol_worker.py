
from time import sleep

import grpc
import paho.mqtt.client as mqtt
import urllib.parse

from worker import accesscontrol_pb2 as accesscontrol__pb2

def mqtt_publish(mqtt_client, topic, payload):
    mqtt_client.publish(topic=topic, payload=payload)



class AccessControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DingDong(self, request, context):
        """Missing associated documentation comment in .proto file."""

        print(request)
        return_message = accesscontrol__pb2.DingDongReply(message="SERVER SIER HEI")
        return return_message
        
        # context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        # context.set_details('Method not implemented!')
        # raise NotImplementedError('Method not implemented!')


    def __init__(self, client_id=None, config=None):
        print(client_id)
        self._mqttc = mqtt.Client(client_id)
        self._config = config
        # self._lockhandler = LockActuator()
        # self._bellhandler = BellHandler(config['bell'])
        self._mqttc.on_message = self.mqtt_on_message
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_publish = self.mqtt_on_publish
        self._mqttc.on_subscribe = self.mqtt_on_subscribe

    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))
        print(f"flag: {flags}")

    def mqtt_on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def mqtt_on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def mqtt_on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def mqtt_on_log(self, mqttc, obj, level, string):
        print(string)

    def tls_set(self):
        #TODO: sett ssl and cert for encrypt
        pass


    def connect_to_broker(self, host, port, username=None, password=None):
        print(f"connecting to host {host}")
        print(f"Username: {username}, Password: {password}")
        # server_parsed = urllib.parse.urlparse(server)
        self._mqttc.username_pw_set(username, password=password)
        self._mqttc.connect(host=host, port=port, keepalive=60)


    def subscribe(self):
        pass
        # for door in self._config:
        #     topic = self._config[door]["command_topic"]
        #     print(f"subscribing to topic: {topic}")
        #     self._mqttc.subscribe(topic, qos=0)



    def run(self):     
        # rc = 0
        # while rc == 0:

        #     rc = self._mqttc.loop()

        # return rc
        self._mqttc.loop_start()
