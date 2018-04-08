FROM ubuntu:16.04

LABEL name="ssis-dashboard" version="0.6.8" maintainer="Davide Mauri <info@davidemauri.it>"

# apt-get and system utilities
RUN apt-get update && apt-get install -y \
    curl apt-utils apt-transport-https debconf-utils gcc build-essential g++-5 \
    software-properties-common python-software-properties \
    && rm -rf /var/lib/apt/lists/*

# Microsoft repository for odbc driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# install SQL Server drivers
RUN apt-get update && ACCEPT_EULA=Y apt-get -y install msodbcsql 
RUN apt-get -y install unixodbc unixodbc-dev

# repository for python 3.6
RUN add-apt-repository ppa:jonathonf/python-3.6

# install python 3.6
RUN apt-get update && apt-get install -y python3.6 python3-pip

# install necessary locales
RUN apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen

# cleanup
RUN apt-get autoremove -y

# upgrade pip
RUN pip3 install --upgrade pip

# install ssis-dashboard
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=dashboard/__init__.py LC_ALL=C.UTF-8 LANG=C.UTF-8
EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0" ]

