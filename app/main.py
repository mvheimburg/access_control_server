
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mvheimburg'

from concurrent import futures
import sys
from os import environ, path

import grpc
import yaml

from pythonpath import add_dir_to_pythonpath


def main(mode=0):
    """
    Main function. 
    
    """
    from worker import MqttWorker, MqttGuideServicer
    from worker import mqttguide_pb2_grpc as mqttguide_pb2__grpc

    from definitions import ROOT_DIR

    ### Get from config somehow #############################
    secret_cfg_path = path.join(ROOT_DIR, "secrets.yaml")
    with open(secret_cfg_path, 'r') as stream:
        secret_cfg = yaml.load(stream, Loader=yaml.FullLoader)
    print(secret_cfg)
    server = secret_cfg['mqtt']['server']
    uname = secret_cfg['mqtt']['username']
    password = secret_cfg['mqtt']['password']
    client_id = secret_cfg['mqtt']['client_id']
    ########################################################


    cfg = None
    cfg_path = path.join(ROOT_DIR, "config.yaml")
    with open(cfg_path, 'r') as stream:
        cfg = yaml.load(stream, Loader=yaml.FullLoader)
    print(cfg)

    # mqttworker = MqttWorker(client_id=client_id, config=cfg)
    # mqttworker.connect_to_broker(server, uname, password)
    # mqttworker.subscribe()
    # mqttworker.run()

    mqttworker = MqttGuideServicer(client_id=client_id, config=cfg)
    mqttworker.connect_to_broker(server, uname, password)
    mqttworker.subscribe()
    mqttworker.run()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mqttguide_pb2__grpc.add_MqttGuideServicer_to_server(
        mqttworker, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()




if __name__ == "__main__":

    mode = 0

    if 'local' in sys.argv:
        mode = 1

    add_dir_to_pythonpath()
    main(mode=mode)