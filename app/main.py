
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

    cfg = None
    cfg_path = path.join(ROOT_DIR, "config.yaml")
    with open(cfg_path, 'r') as stream:
        cfg = yaml.load(stream, Loader=yaml.FullLoader)
    print(cfg)

    # ### Get from config somehow #############################
    secret_cfg_path = path.join(ROOT_DIR, "secrets.yaml")

    import os.path
    if path.isfile(secret_cfg_path):
        with open(secret_cfg_path, 'r') as stream:
            secret_cfg = yaml.load(stream, Loader=yaml.FullLoader)
        print(secret_cfg)
        host = secret_cfg['mqtt']['server']
        uname = secret_cfg['mqtt']['username']
        password = secret_cfg['mqtt']['password']
        client_id = secret_cfg['mqtt']['client_id']
        port = secret_cfg['mqtt']['port']
    # ########################################################
    else:
        host = cfg['secrets']['mqtt']['server']
        uname = cfg['secrets']['mqtt']['username']
        password = cfg['secrets']['mqtt']['password']
        client_id = cfg['secrets']['mqtt']['client_id']
        port = cfg['secrets']['mqtt']['port']
        
    port = int(port)
    print(f'host is: {host}')
    print(f'uname is: {uname}')
    print(f'password is: {password}')
    print(f'client_id is: {client_id}')
    print(f'port is: {port}')
    print(f'port type is: {type(port)}')
    # mqttworker = MqttWorker(client_id=client_id, config=cfg)
    # mqttworker.connect_to_broker(server, uname, password)
    # mqttworker.subscribe()
    # mqttworker.run()

    mqttworker = MqttGuideServicer(client_id=client_id, config=cfg)
    mqttworker.connect_to_broker(host, port, uname, password)
    mqttworker.subscribe()
    mqttworker.run()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mqttguide_pb2__grpc.add_MqttGuideServicer_to_server(
        mqttworker, server)
    server.add_insecure_port('[::]:5055')
    server.start()
    server.wait_for_termination()




if __name__ == "__main__":

    mode = 0

    if 'local' in sys.argv:
        mode = 1

    add_dir_to_pythonpath()
    main(mode=mode)