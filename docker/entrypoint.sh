#!/bin/bash

JUPYTER="python -m jupyter notebook --config=/opt/conf/jupyter_notebook_config.py"
ETL="/opt/etl/components/bash/workshop.sh"

function exec_action(){
    if [ "jupyter" == "$1" ]; then
        echo "[INFO] Starting Jupyter notebooks server ..."
        /bin/bash -c "$JUPYTER"
    elif [ "etl" == "$1" ]; then
        echo "[INFO] Running Demo ETL ..."
        /bin/bash -c "$ETL"
    else
        echo "Usage: $0 jupyter|etl"
        /bin/bash
    fi
}


echo "[INFO] Starting Spark history server ..."
${SPARK_HOME}/sbin/start-history-server.sh --properties-file ${SPARK_HOME}/conf/spark-defaults.conf
echo "[INFO] Spark History Server listening at http://localhost:4040/"

exec_action $1

echo "[INFO] Stopping Spark history server ..."
${SPARK_HOME}/sbin/stop-history-server.sh

echo "[INFO] Done!!"