import os
import numbers_pb2
import numbers_pb2_grpc
import time
import grpc


def run():
    number = int(input("Enter number: "))

    with grpc.insecure_channel("localhost:9999") as channel:
        stub = numbers_pb2_grpc.OperationsStub(channel)

        while True:
            try:
                response = stub.DoOps(numbers_pb2.Number(value=number))
                print(response)
                break
            except KeyboardInterrupt:
                print("BRUH")
                channel.unsubscribe(close)
                exit()


def close(channel):
    channel.close()


if __name__ == "__main__":
    run()