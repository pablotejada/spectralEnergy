from flask import Flask, jsonify, render_template
import grpc
# import meterusage_pb2
# import meterusage_pb2_grpc

app = Flask(__name__)
# grpc_channel = grpc.insecure_channel('localhost:50051')  # Assuming gRPC server is running locally on port 50051
# grpc_stub = meterusage_pb2_grpc.MeterUsageServiceStub(grpc_channel)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    # response = grpc_stub.GetMeterUsage(meterusage_pb2.Timestamp())
    # data = [{"timestamp": item.timestamp, "usage": item.usage} for item in response]
    data = {
        "k1": 1, 
        "k2": 2, 
        "k3": 3,       
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
