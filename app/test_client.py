
import grpc

from worker.accesscontrol_pb2_grpc import AccessControlStub
from worker.accesscontrol_pb2 import DingDongRequest


channel = grpc.insecure_channel('127.0.0.1:5055')
stub = AccessControlStub(channel)

request=DingDongRequest(message="Python test client")
message = stub.DingDong(request=request)

print(message)




