# Using Python v3.9.13 as base image.
FROM python:3.9

# Defining Apache Spark framework.
ENV SPARK_VERSION=3.2.1

# Setting the folder /opt as the working directory.
WORKDIR /opt/

# Downloading/Installing the linux dependencies required for the processes held here.
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
COPY ./docker/requirements.txt ./docker/jupyter_notebook_config.py /opt/conf/

# Installing the applications Python dependencies.
RUN pip install -r /opt/conf/requirements.txt && \
    pip install jupyter notebook ipykernel ipython

# Installing Apache Spark
RUN curl http://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz | tar -zx
RUN ln -s /opt/spark-${SPARK_VERSION}-bin-hadoop2.7 /usr/local/spark

# Creating the folder that are going to be used.
RUN mkdir -p /tmp/spark/events /opt/etl/data/output/results && \
    chmod -R 750 /tmp /opt/etl /opt/etl/data/output/results

# Setting the environment variables needed for Spark to work.
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
ENV SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop2.7
ENV SPARK_OPTS=--driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info 
ENV PATH=${SPARK_HOME}/bin:$HOME/.local/bin:$PATH

# Copying the Spark custom configuration.
COPY ./docker/spark-defaults.conf ${SPARK_HOME}/conf/
COPY ./workshop.sh ./Makefile ./pyproject.toml /opt/etl/
COPY ./components/ /opt/etl/components/ 
COPY ./data/ /opt/etl/data/ 

# Opening port for Spark History server
EXPOSE 4040

# Opening port for Jupyter server
EXPOSE 8000 

# Defining the command that is going to be executed once the container startup,
# this command can be overriden once a new entrypoint is defined within the 
# docker run command. 
CMD [ "python", "-m", "jupyter", "notebook", "--config=/opt/conf/jupyter_notebook_config.py" ]
