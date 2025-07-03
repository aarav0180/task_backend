# Coding Agent with Orchestration

## Features

- Secure sandboxed agent (Jupyter, xdot, VNC, shell, code exec, filesystem)
- Orchestration server with /schedule and /status/:id
- Live VNC via noVNC
- Context management for large tasks
- Scalable via Kubernetes

## Quick Start

1. Build agent container:
   docker build -t agent:latest .

2. Run orchestration server:
   cd server
   pip install -r requirements.txt
   uvicorn main:app --host 0.0.0.0 --port 5000

3. Schedule a job:
   curl -X POST http://localhost:5000/schedule -H "Content-Type: application/json" -d '{"task":"Build me a todo app in React"}'

4. Access VNC: http://localhost:8080/vnc.html

## Kubernetes

See k8s/job.yaml for an example job spec.
