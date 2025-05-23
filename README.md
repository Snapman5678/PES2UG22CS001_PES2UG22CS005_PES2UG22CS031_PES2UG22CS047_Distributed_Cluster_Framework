# NexusCore - Resource Monitoring Framework

A lightweight distributed system framework focused on CPU and memory resource management in containerized environments.

## Features

- Real-time CPU and memory monitoring
- Resource-aware pod scheduling
- Resource utilization tracking and limits
- Simple fault detection for resource exhaustion
- Docker-based node simulation

## Architecture

- **Core Components**
  - Resource Monitor: Tracks CPU cores and memory usage
  - Scheduler: Places pods based on available CPU and memory
  - Resource Failure Handler: Detects and handles resource exhaustion

- **APIs**
  - `/nodes`: Manage compute nodes and their resources
  - `/pods`: Deploy and manage pods with resource requirements
  - `/health`: Monitor cluster and node resource utilization
  - `/host`: Track host system resource constraints

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the system:
```bash
docker-compose up -d
```

3. Add a node (example with 2 CPU cores and 2GB RAM):
```bash
python -m cli.main nodes add --cpu 2 --memory 2048
```

4. Create a pod:
```bash
python -m cli.main pods create --name test-pod --cpu 1 --memory 512
```

5. Monitor cluster health:
```bash
python -m cli.main cluster health
```

## Resource Management

- **CPU Tracking**
  - Measured in cores
  - Allocation based on available CPU cores
  - Usage limits to prevent overload

- **Memory Management**
  - Tracked in bytes/megabytes
  - Real-time available memory monitoring
  - Overcommit protection

## CLI Commands

- `nodes list`: Show all nodes with resource usage
- `pods list`: List all pods and their resource allocations
- `cluster health`: Display cluster-wide resource metrics
- `cluster limits`: Update resource usage limits

## Testing

Run the load testing script to simulate resource pressure:
```bash
python scripts/load_test.py
```
