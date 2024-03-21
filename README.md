

# Meter Usage Application Spectral Energy

This repository contains the code for a meter usage application consisting of a server and a client component.

## Setup

Follow these steps to set up and run the application:

### 1. Create Virtual Environment

```bash
python3 -m venv venv
```
### 2. Activate Virtual Environment
On Windows:
```bash
venv\Scripts\activate
```

On Unix or MacOS:
```bash
source venv/bin/activate
```

### 3. Install requirements
```
pip install -r requirements.txt
```

### 4. Run Server
```bash
cd  spectralEnergy/grpc_server/
python meterusage_server.py
```

### 5. Run Client
```bash
cd spectralEnergy/flask_client/
python app.py
```

### 6. Browse Application
Browse [localhost:5000](localhost:5000)