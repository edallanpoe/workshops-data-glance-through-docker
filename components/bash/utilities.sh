#!/bin/bash
CONST_APP_DONE=0
CONST_APP_ERROR=1
CONST_COLOR_YELLOW=1
CONST_COLOR_BLUE=2
CONST_COLOR_GREEN=3
CONST_COLOR_RED=4
CONST_COLOR_WHITE=5
ETL_PATH=/opt/etl


function echo_color(){
	local typec=$1
	local text=$2

	if [ $typec -eq $CONST_COLOR_YELLOW ]; then
		echo -e "\e[0;33m$text\e[0m"
	elif [ $typec -eq $CONST_COLOR_BLUE ]; then
		echo -e "\e[0;34m$text\e[0m"
	elif [ $typec -eq $CONST_COLOR_GREEN ]; then
		echo -e "\e[0;32m$text\e[0m"
	elif [ $typec -eq $CONST_COLOR_RED ]; then
		echo -e "\e[0;31m$text\e[0m"	
	elif [ $typec -eq $CONST_COLOR_WHITE ]; then
		echo -e "\e[0;39m$text\e[0m"	
	fi
}

function execute_code(){
	path_code=$1
	echo $path_code
	APP_STATE=$CONST_APP_DONE

	# code validation
	sep_step
	echo_color  $CONST_COLOR_YELLOW "[STEP 01] cleaning pyc files ......... [VALIDATING]"
	cd $ETL_PATH ; make clean etl_path=$ETL_PATH ; cd -
	echo_color  $CONST_COLOR_GREEN  "[STEP 01] ............................ [OK]"

	sep_step
	echo_color  $CONST_COLOR_YELLOW "[STEP 02] validating mypy ............ [VALIDATING]"
	cd $ETL_PATH ; make mypy path_code=$path_code ; cd -
	if [ $? -eq 2 ]; then
		echo_color  $CONST_COLOR_RED  "[STEP 02] ............................ [FAIL]"
		APP_STATE=$CONST_APP_ERROR
	else
		echo_color  $CONST_COLOR_GREEN  "[STEP 02] ............................ [OK]"
	fi

	sep_step
	echo_color  $CONST_COLOR_YELLOW "[STEP 03] validating flake8 .......... [VALIDATING]"
	cd $ETL_PATH ; make lint path_code=$path_code ; cd -
	if [ $? -eq 2 ]; then
		echo_color  $CONST_COLOR_RED  "[STEP 03] ............................ [FAIL]"
		APP_STATE=$CONST_APP_ERROR
	else
		echo_color  $CONST_COLOR_GREEN  "[STEP 03] ............................ [OK]"
	fi

	sep_step
	echo_color  $CONST_COLOR_YELLOW "[STEP 04] cleaning mypy files flake8 ..... [VALIDATING]"
	make clean-mypy etl_path=$ETL_PATH
	echo_color  $CONST_COLOR_GREEN  "[STEP 04] ............................ [OK]"

	sep_step
	echo "code validation has finished, execution state:" 
	echo ""
	if [ $APP_STATE -eq $CONST_APP_ERROR ]; then
		echo -e "APP STATE : \e[0;31m FAIL \e[0m"
		echo -e "APP CODE  : \e[0;31m -1 \e[0m"  
	else
		echo -e "APP STATE : \e[0;32m OK \e[0m" 
		echo -e "APP CODE  : \e[0;32m 0 \e[0m"
	fi

}

function run_process(){
	gpx=$1

	sep_step
	echo_color  $CONST_COLOR_YELLOW "validating ......... [$gpx]"

	parameters=$(python -c "path='$gpx'; print(','.join(path.split('/')[-3:]))")
    vehicule_type=$(echo $parameters | awk -F ',' '{print $1}')
    vehicule_id=$(echo $parameters | awk -F ',' '{print $2}')
    date_gpx=$(echo $parameters | awk -F ',' '{print $3}' |  awk -F '.' '{print $2}')

    python $ETL_PATH/components/python/app.py run-process --gpx-file $gpx \
        --vehicle-type  $vehicule_type\
        --vehicle-id $vehicule_id \
        --event-date $date_gpx \
        --output "$ETL_PATH/data/output"

   if [ $? -ne 0 ]; then
		echo_color  $CONST_COLOR_RED  "[$gpx] ......... [FAIL]"
		APP_STATE=$CONST_APP_ERROR
	else
		echo_color  $CONST_COLOR_GREEN  "[$gpx] ............... [OK]"
	fi
}

function run_spark(){
	app_path=$1
	spark-submit --master local[4] --name demo \
		$ETL_PATH/components/spark/spark-job.py \
  		$app_path/data/output/files \
  		$app_path/data/output/results \
  		$app_path/data/parametric/gas_consumption.json
}

function press_to_continue(){
	echo ""
	read -p "press enter to continue ..."
}

function secure_exit(){
	while true; do
		echo     "---------------------"
		echo -en "press Q or q to exit: "
		read input
		if [[ $input = "q" ]] || [[ $input = "Q" ]] 
			then break 
		else 
			echo "invalid input."
		fi
	done
}

function run_report(){
	app=$1
	sep_step
	echo_color  $CONST_COLOR_YELLOW "validating ......... [REPORTS]"

    python $app/components/python/app.py generate-report \
    	--images-path  $app/data/output/images \
    	--consolidated-file $app/data/output/results/parquet/consolidated/*.parquet

   if [ $? -ne 0 ]; then
		echo_color  $CONST_COLOR_RED  "[REPORTS] ......... [FAIL]"
		APP_STATE=$CONST_APP_ERROR
	else
		echo_color  $CONST_COLOR_GREEN  "[REPORTS] ............... [OK]"
	fi
}


