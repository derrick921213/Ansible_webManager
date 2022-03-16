FROM almalinux:latest
WORKDIR /code
COPY . /code
RUN dnf install epel-release python39 python39-pip -y &&dnf install -y  openssl-devel bzip2-devel libffi-devel zlib-devel ncurses-devel gdbm-devel nss-devel readline-devel sqlite-devel &&python3.9 -m pip install -U pip && python3.9 -m pip install setuptools-rust wheel && python3.9 -m pip install -r requirements.txt
RUN 
ENTRYPOINT ["./start.sh"] 

