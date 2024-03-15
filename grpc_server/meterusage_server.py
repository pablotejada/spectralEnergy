import grpc
from concurrent import futures
import meterusage_pb2
import meterusage_pb2_grpc
import csv
import json


# import meterusage_pb2
# import meterusage_pb2_grpc


# grpc_channel = grpc.insecure_channel('localhost:50051')  # Assuming gRPC server is running locally on port 50051
# grpc_stub = meterusage_pb2_grpc.MeterUsageServiceStub(grpc_channel)

class MeterUsageService(meterusage_pb2_grpc.MeterUsageServiceServicer):
    def GetMeterUsage(self, request, context):
        meter_usage_list = []
        with open('meterusage.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                meter_usage_list.append(meterusage_pb2.MeterUsage(
                    time=row['time'],
                    meterusage=float(row['meterusage'])
                ))
        return meterusage_pb2.MeterUsageResponse(meter_usage=meter_usage_list)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meterusage_pb2_grpc.add_MeterUsageServiceServicer_to_server(MeterUsageService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started. Listening on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
