

# Meter Usage Application Spectral Energy

This repository contains the code for a meter usage application consisting of a server and a client component.

## Setup

Follow these steps to set up and run the application:

### 1. Create Virtual Environment

```bash
python3 -m venv venv
```
## Activate Virtual Environment
On Windows:
```bash
venv\Scripts\activate
```

On Unix or MacOS:
```bash
source /venv/bin/activate
```

## Install requirements
```
pip install -r requirements.txt
```

## Run Server
```bash
python spectralEnergy/flask_client/app.py
```

## Run Client
```bash
python spectralEnergy/grpc_server/meterusage_server.py
```

## Browse Application
Browse [localhost:5000](localhost:5000)