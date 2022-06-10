# Allows to create different builds using different platforms if the base image multiple platforms.
# ARG Ref: https://docs.docker.com/engine/reference/builder/#arg
ARG PLATFORM

# Using Python v3.9.13 as base image.
# Creating a base image: https://docs.docker.com/develop/develop-images/baseimages/
# FROM Ref: https://docs.docker.com/engine/reference/builder/#from
# Image in Docker Hub: https://hub.docker.com/layers/python/library/python/3.9/images/sha256-2c9cc527cde7305aad12bbdcfb3b5ee51d6e95d8fae91054a1d960942e385521?context=explore
FROM --platform=${PLATFORM} python:3.9

# Defining Apache Spark framework.
# ENV Ref: https://docs.docker.com/engine/reference/builder/#env
ENV SPARK_VERSION=3.2.1

# Setting the folder /opt as the working directory.
# WORKDIR Ref: https://docs.docker.com/engine/reference/builder/#workdir
WORKDIR /opt/

# Downloading/Installing the linux dependencies required for the processes held here.
# As this is a linux based image, it runs by default on /bin/sh shell.
# But it can be changed by setting /bin/bash -c "command..." instead.
# RUN Ref: https://docs.docker.com/engine/reference/builder/#run
RUN apt update && \
    apt install -y wkhtmltopdf pv tree make binutils build-essential gcc openjdk-11-jdk openjdk-11-jre \
        ca-certificates-java libpq-dev libproj-dev proj-bin libgdal-dev gdal-bin && \
    apt clean && \
    update-ca-certificates -f

# Installing the Python dependencies.
RUN python -m pip install --upgrade pip wheel && \
    pip install pyproj==3.2.1 --no-binary pyproj && \
    pip install setuptools==57.5.0 && \
    pip install pygdal==3.2.2.10 && \
    pip install --upgrade setuptools

# Copying the required files for supporting either the jupytr server and the ETL process.
# COPY Ref: https://docs.docker.com/engine/reference/builder/#copy
COPY ./docker/requirements.txt ./docker/jupyter_notebook_config.py /opt/conf/

# Installing the applications Python dependencies.
RUN pip install -r /opt/conf/requirements.txt && \
    pip install jupyter notebook ipykernel ipython

# Installing Apache Spark
RUN curl http://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz | tar -zx
RUN ln -s /opt/spark-${SPARK_VERSION}-bin-hadoop2.7 /usr/local/spark

# Copying the Spark custom configuration.
COPY ./Makefile ./pyproject.toml /opt/etl/
COPY ./components/ /opt/etl/components/ 
COPY ./data/ /opt/etl/data/
COPY ./docker/entrypoint.sh /opt/
COPY ./docker/spark-defaults.conf /opt/spark-${SPARK_VERSION}-bin-hadoop2.7/conf/

# Creating the folder that are going to be used.
RUN mkdir -p /tmp/spark/events /opt/etl/data/output/results && \
    chmod -R 750 /tmp /opt/etl /opt/etl/data/output/results /opt/entrypoint.sh /opt/etl/components/

# Setting the environment variables needed for Spark to work.
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
ENV SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop2.7
ENV SPARK_OPTS=--driver-java-options=-Xms1024M --driver-java-options=-Xmx2048M --driver-java-options=-Dlog4j.logLevel=info 
ENV PATH=${SPARK_HOME}/bin:$HOME/.local/bin:$PATH

# Opening port for Spark History server
# EXPOSE Ref: https://docs.docker.com/engine/reference/builder/#expose
EXPOSE 4040

# Opening port for Jupyter server
EXPOSE 8000 

# Sets the entrypoint
# ENTRYPOINT Ref: https://docs.docker.com/engine/reference/builder/#entrypoint
ENTRYPOINT [ "/opt/entrypoint.sh" ]
