FROM python:3.9

ENV SPARK_VERSION=3.2.1
ENV TINI_VERSION=v0.6.0

WORKDIR /opt/

COPY ./docker/requirements.txt ./docker/jupyter_notebook_config.py /opt/conf/

RUN apt update && \
    apt install -y openjdk-11-jdk openjdk-11-jre ca-certificates-java && \
    apt clean && \
    update-ca-certificates -f
RUN python -m pip install --upgrade pip && \
    pip install -r /opt/conf/requirements.txt
RUN pip install jupyter ipykernel ipython
RUN curl http://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz | tar -zx
RUN ln -s /opt/spark-${SPARK_VERSION}-bin-hadoop2.7 /usr/local/spark

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
ENV SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop2.7
ENV SPARK_OPTS=--driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info 
ENV PATH=${SPARK_HOME}/bin:$HOME/.local/bin:$PATH
# ENV PYSPARK_DRIVER_PYTHON="python"
# ENV PYSPARK_DRIVER_PYTHON_OPTS="-m jupyter notebook --config=/opt/conf/jupyter_notebook_config.py"

EXPOSE 9999:80
EXPOSE 4040:4040

# CMD [ "pyspark" ]
CMD [ "python", "-m", "jupyter", "notebook", "--config=/opt/conf/jupyter_notebook_config.py" ]
