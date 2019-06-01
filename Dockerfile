FROM ubuntu

RUN apt update
RUN apt install -y git curl unzip tar g++ make
RUN git clone https://github.com/microsoft/vcpkg.git /ws/vcpkg
RUN /ws/vcpkg/bootstrap-vcpkg.sh
