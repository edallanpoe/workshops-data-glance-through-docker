# Using Python v3.9.13 as base image.
# Ref: https://docs.docker.com/engine/reference/builder/#from
FROM python:3.9

# Defining Apache Spark framework.
# Ref: https://docs.docker.com/engine/reference/builder/#env
ENV SPARK_VERSION=3.2.1

# Setting the folder /opt as the working directory.
# Ref: https://docs.docker.com/engine/reference/builder/#workdir
WORKDIR /opt/

# Downloading/Installing the linux dependencies required for the processes held here.
# Ref: https://docs.docker.com/engine/reference/builder/#run
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
# Ref: https://docs.docker.com/engine/reference/builder/#copy
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
# Ref: https://docs.docker.com/engine/reference/builder/#expose
EXPOSE 4040

# Opening port for Jupyter server
EXPOSE 8000 

# Sets the entrypoint
# Ref: https://docs.docker.com/engine/reference/builder/#entrypoint
ENTRYPOINT [ "/opt/entrypoint.sh" ]
