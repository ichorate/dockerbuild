FROM ubuntu

RUN apt update
RUN apt install -y wget tar
WORKDIR /usr/src
RUN wget https://github.com/cdr/code-server/releases/download/1.1119-vsc1.33.1/code-server1.1119-vsc1.33.1-linux-x64.tar.gz
RUN tar -xf code-server1.1119-vsc1.33.1-linux-x64.tar.gz
RUN cp code-server1.1119-vsc1.33.1-linux-x64/code-server /usr/local/bin
