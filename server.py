from concurrent import futures
import grpc
import numbers_pb2
import numbers_pb2_grpc
from do_operations import do_operations
import time


class Listener(numbers_pb2_grpc.OperationsServicer):
    def __init__(self, *args, **kwargs):
        pass

    def DoOps(self, request, context):
        tupl = do_operations(request.value)

        return numbers_pb2.Result(
            add=tupl[0],
            subtract=tupl[1],
            multiply=tupl[2],
            division=int(tupl[3])
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    numbers_pb2_grpc.add_OperationsServicer_to_server(Listener(), server)

    server.add_insecure_port("[::]:9999")
    server.start()


if __name__ == "__main__":
    while True:
        serve()
