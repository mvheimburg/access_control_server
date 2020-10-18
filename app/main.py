
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mvheimburg'

from concurrent import futures
import sys
from os import environ, path

import flask
from flask import request, jsonify
from flask_cors import CORS

import grpc
import yaml

from pythonpath import add_dir_to_pythonpath

data = [
    {'id': 0,
     'mac': 1234,
     'level': 1},
    {'id': 1,
     'mac': 4567,
     'level': 3},
]




def main(mode=0):
    """
    Main function. 
    
    """
    from definitions import ROOT_DIR

    app = flask.Flask(__name__)
    CORS(app)
    app.config["DEBUG"] = True  

    from worker import AccessControlWorker

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
        host = secret_cfg['mqtt']['host']
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

    worker = AccessControlWorker(client_id=client_id, config=cfg)
    # mqttworker.connect_to_broker(host, port, uname, password)
    # mqttworker.subscribe()
    # mqttworker.run()

    @app.route('/', methods=['GET'])
    def home():
        return '''<h1>Distant Reading Archive</h1>
        <p>A prototype API for distant reading of science fiction novels.</p>'''


    @app.route('/resources/data/all', methods=['GET'])
    def api_all():
        print('getting api_all')
        return jsonify(data)


    @app.route('/resources/data', methods=['GET'])
    def api_id():
        # Check if an ID was provided as part of the URL.
        # If ID is provided, assign it to a variable.
        # If no ID is provided, display an error in the browser.
        print('getting api_id')
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."

        # Create an empty list for our results
        results = []    
       # Loop through the data and match results that fit the requested ID.
        # IDs are unique, but other fields might return many results
        for book in data:
            if book['id'] == id:
                results.append(book)

        # Use the jsonify function from Flask to convert our list of
        # Python dictionaries to the JSON format.
        return jsonify(results)



    app.run()


if __name__ == "__main__":

    mode = 0

    if 'local' in sys.argv:
        mode = 1

    add_dir_to_pythonpath()
    main(mode=mode)