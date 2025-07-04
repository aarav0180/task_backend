# Task Backend Project

## Overview
This project provides a containerized development environment with a Linux desktop, JupyterLab, and web-based VNC access. It is designed for running Python code, developing and testing backend services, and remote desktop access via browser.

## Features & Technologies Used
- **Base Image:** Ubuntu 22.04
- **Python 3 & pip:** For running Python scripts and JupyterLab
- **Node.js & npm:** For JavaScript/TypeScript support
- **JupyterLab:** Interactive Python development and notebooks
- **noVNC & x11vnc:** Web-based VNC access to the Linux desktop
- **Fluxbox:** Lightweight window manager for the desktop environment
- **Supervisor:** Process control system to manage multiple services
- **Docker:** Containerization for easy deployment and reproducibility
- **Other Tools:** xvfb, xdotool, wget, curl, git, net-tools, dos2unix

## Architecture
```
-------------------
|    Docker Image   |
-------------------
| Ubuntu 22.04      |
| Python 3, pip     |
| Node.js, npm      |
| JupyterLab        |
| noVNC, x11vnc     |
| Fluxbox           |
| Supervisor        |
-------------------
        |
        v
-------------------
|  Exposed Ports    |
|-------------------|
| 8080: noVNC (web) |
| 8888: JupyterLab  |
| 5900: VNC server  |
| 5000: FastAPI     |
-------------------
```

- **Supervisor** starts and manages JupyterLab, noVNC, x11vnc, Fluxbox, and Xvfb.
- **noVNC** provides browser-based access to the Linux desktop (port 8080).
- **JupyterLab** is available for interactive Python development (port 8888).
- **VNC** can be accessed directly with a VNC client (port 5900).
- **FastAPI** backend is available on port 5000.

## Directory Structure
```
task_backend/
├── Dockerfile
├── entrypoint.sh
├── supervisord.conf
├── project.txt
├── README.md
├── k8s/
│   └── job.yaml
└── server/
    ├── main.py
    └── requirements.txt
```

## How to Build and Run

### 1. Build the Docker Image
Open a terminal in the `task_backend` directory and run:
```sh
docker build -t agent:latest .
```

### 2. Run the Container
```sh
docker run -it --rm -p 8080:8080 -p 8888:8888 -p 5900:5900 -p 5000:5000 agent:latest
```

### 3. Access the Services
- **Linux Desktop (via browser):** http://localhost:8080
- **JupyterLab:** http://localhost:8888
- **VNC (with client):** localhost:5900
- **FastAPI Backend:** http://localhost:5000

### 4. Running Python Code
- Use JupyterLab to create and run Python notebooks.
- To run a script (e.g., `main.py`):
  - Open a terminal in JupyterLab or connect to the container shell.
  - Run: `python3 /home/agent/workspace/server/main.py`
- To run the FastAPI backend server:
  - Open a terminal and run:
    ```sh
    cd /home/agent/workspace/server
    pip install -r requirements.txt
    uvicorn main:app --host 0.0.0.0 --port 5000
    ```

## Customization
- Add your Python code and dependencies in the `server/` directory.
- Update `supervisord.conf` to manage additional services or scripts.
- Modify the Dockerfile to install extra packages as needed.

## Kubernetes
- A sample Kubernetes job manifest is provided in `k8s/job.yaml` for deployment in a K8s cluster.

## License
Specify your license here.

---
For questions or contributions, please open an issue or pull request.
