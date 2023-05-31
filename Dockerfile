FROM node:bullseye

RUN dpkg --add-architecture i386
RUN apt-get -y update
RUN apt-get -y install python3 python3-pip wine xvfb openssl wine32:i386

# RUN python3 -m pip install pefile distorm3 pycrypt

COPY metatwin.py /usr/app/tools/

COPY ResourceHacker.exe /usr/app/tools/
COPY sigthief.py /usr/app/tools/
# COPY sigvalidator.py /usr/app/tools

# Source Executable
COPY ADExplorer64.exe /usr/app/tools

# Target Executable
# COPY executable.exe /usr/app/tools

RUN chmod +x /usr/app/tools/sigthief.py
RUN chmod +x /usr/app/tools/metatwin.py

RUN ln -s /usr/app/tools/sigthief.py /usr/local/bin/sigthief
RUN ln -s /usr/app/tools/metatwin.py /usr/local/bin/metatwin

RUN chmod +x /usr/local/bin/sigthief
RUN chmod +x /usr/local/bin/metatwin

WORKDIR /usr/app/tools
