FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y sudo python3 python3-pip nodejs npm \
    xvfb x11vnc fluxbox xdotool wget curl git \
    supervisor net-tools dos2unix && \
    pip3 install jupyterlab && \
    npm install -g typescript && \
    useradd -ms /bin/bash agent && \
    mkdir -p /home/agent/workspace && \
    chown -R agent:agent /home/agent

RUN git clone https://github.com/novnc/noVNC.git /opt/novnc && \
    git clone https://github.com/novnc/websockify /opt/novnc/utils/websockify

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY entrypoint.sh /entrypoint.sh
RUN dos2unix /entrypoint.sh || true
RUN chmod +x /entrypoint.sh

USER agent
WORKDIR /home/agent/workspace

EXPOSE 8080 5900 8888

ENTRYPOINT ["/entrypoint.sh"]
