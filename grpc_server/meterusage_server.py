import grpc
import meterusage_pb2
import meterusage_pb2_grpc
from concurrent import futures


class MeterUsageServicer(meterusage_pb2_grpc.MeterUsageServiceServicer):
    def GetMeterUsage(self, request, context):
        with open("meterusage.csv", "r") as file:
            csv_content = file.read()
        yield meterusage_pb2.MeterUsage(csv_content=csv_content)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meterusage_pb2_grpc.add_MeterUsageServiceServicer_to_server(MeterUsageServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
