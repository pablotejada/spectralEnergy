from flask import Flask, jsonify, render_template
import grpc
import os
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    response = grpc_stub.GetMeterUsage(meterusage_pb2.Timestamp())
    data = [{"timestamp": item.timestamp, "usage": item.usage} for item in response]
    # data = {
    #     "k1": 1, 
    #     "k2": 2, 
    #     "k3": 3,       
    # }
    return jsonify(data)

if __name__ == '__main__':
    # Get the absolute path of the current directory


    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Get the absolute path of folder0
    folder0_path = os.path.abspath(os.path.join(current_dir, '..'))
    sys.path.append(os.path.abspath(os.path.join(folder0_path, 'grpc_server')))

    # Append folder0 to sys.path if it's not already there
    if folder0_path not in sys.path:
        sys.path.append(folder0_path)

    from grpc_server import meterusage_pb2, meterusage_pb2_grpc
    grpc_channel = grpc.insecure_channel('localhost:50051')  # Assuming gRPC server is running locally on port 50051
    grpc_stub = meterusage_pb2_grpc.MeterUsageServiceStub(grpc_channel)
    
    app.run(debug=True)
