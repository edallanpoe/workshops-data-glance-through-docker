#!/bin/bash

APP=$(dirname $(realpath $0))

source $APP/components/bash/utilities.sh
source $APP/components/bash/printer.sh

function run_welcome(){
   cat $APP/data/animations/movglobe.vt | pv -q -L 9600
   clear
   demo_welcome
   demo_body
   press_to_continue
}

function run_stage_0(){
   make clean
   stage_0 $APP/data/vehicles
   press_to_continue
   clear
   echo ""
   tree $APP/data/output/results
   press_to_continue
}

function run_stage_1(){
   stage_1
   press_to_continue
   execute_code $APP/components
   press_to_continue
}

function run_stage_2(){
   stage_2
   press_to_continue
   for gpx in $(find $APP | grep -F .gpx); do 
      run_process $gpx 
   done
   echo ""
   echo "SPARK"
   echo ""
   press_to_continue
   run_spark $APP
   press_to_continue
}

function run_stage_3(){
   stage_3
   mkdir -p  $APP/data/output/results/{pdf,pictures} > /dev/null
   press_to_continue
   run_report $APP
   press_to_continue
}

function run_stage_4(){
   stage_4
   echo ""
   tree $APP/data/output/results
   secure_exit
}

run_welcome
run_stage_0
run_stage_1
run_stage_2
run_stage_3
run_stage_4
