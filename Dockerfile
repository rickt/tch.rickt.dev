# base image
FROM ubuntu:24.04

# setup
ENV DEBIAN_FRONTEND=noninteractive

# update the system package lists & install necessary packages
RUN apt-get update && apt-get install -y \
    curl git wget python3-pip python3-venv tzdata \
    && ln -fs /usr/share/zoneinfo/America/Los_Angeles /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# create & activate a virtual environment
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/python -m pip install --upgrade pip

# set the working directory
WORKDIR /app

# copy the requirements file and install Python modules
COPY requirements.txt /app/
RUN /opt/venv/bin/pip install -r requirements.txt

# copy the application code and static folder into the app directory
COPY timecard.py /app/
COPY static/ /app/static/

# expose the application port
EXPOSE 8080

# entry point
CMD ["/opt/venv/bin/python3", "timecard.py"]

# EOF
