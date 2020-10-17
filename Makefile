## Shipping package
## Assumes user is on MacOS, if other OS, please change PROTO_ROOT_DIR to the path of protobuf installation
PROJECT_NAME = access-control

## Dart requires you to manually ship all google provided proto files too.
gendart:
	protoc -I protos/ protos/accesscontrol.proto --plugin=protoc-gen-dart=C:\Users\martinv\AppData\Roaming\Pub\Cache\bin\protoc-gen-dart.bat --dart_out=grpc:protos/generated/dart

genpy:
	python3 -m grpc.tools.protoc -I/protos --python_out=protos/generated/py --grpc_python_out=protos/generated/py protos/mqttguide.proto
	python3 -m grpc.tools.protoc -I protos/ --python_out=protos/generated/py --grpc_python_out=protos/generated/py protos/mqttguide.proto