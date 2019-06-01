FROM codeserver

FROM basedep
RUN apt install -y locales dumb-init net-tools sudo python3 python3-pip
RUN locale-gen en_US.UTF-8
# We unfortunately cannot use update-locale because docker will not use the env variables
# configured in /etc/default/locale so we need to set it manually.
ENV LC_ALL=en_US.UTF-8

RUN adduser --gecos '' --disabled-password coder && \
	echo "coder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd

USER coder
# We create first instead of just using WORKDIR as when WORKDIR creates, the user is root.
RUN mkdir -p /home/coder/project

WORKDIR /home/coder/project

# This assures we have a volume mounted even if the user forgot to do bind mount.
# So that they do not lose their data if they delete the container.
VOLUME [ "/home/coder/project" ]

COPY --from=codeserver  /usr/local/bin/code-server /usr/local/bin/code-server
EXPOSE 8443

ENTRYPOINT ["dumb-init", "code-server", "--allow-http", "--no-auth"]

# preinstall extension.
RUN sudo apt install -y bsdtar
RUN mkdir -p /home/coder/.local/share/code-server/extensions/
WORKDIR /home/coder/.local/share/code-server/extensions/
RUN curl -JL https://marketplace.visualstudio.com/_apis/public/gallery/publishers/twxs/vsextensions/cmake/0.0.17/vspackage \
	| bsdtar -xvf - extension
RUN mv extension twxs.cmake-0.0.17
RUN curl -JL https://github.com/microsoft/vscode-cpptools/releases/download/0.23.1/cpptools-linux.vsix \
	| bsdtar -xvf - extension
RUN mv extension ms-code.cpptools-0.23.1

WORKDIR /home/coder/project
