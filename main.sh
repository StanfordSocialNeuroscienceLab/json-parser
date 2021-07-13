#!/bin/bash

# ------------------------ RUN ME ----------------------
#
# Wraps Python scripts together
# Produces JSON files and CSVs for all standard input JSON files
#
# bash main.sh [ SUBJECT-ID ] [ UP TO THREE (3) JSON FILES ]
#
# Ian Richard Ferguson | Stanford University

if [[ "$#" = 2 ]]; then
    python3 reducer.py $1 $2
    output=`find ./OUTPUT/${1}/ -name '*.json'`
    python3 tabular.py $output

elif [[ "$#" = 3 ]]; then
    python3 reducer.py $1 $2 $3
    output=`find ./OUTPUT/${1}/ -name '*.json'`

    for file in ${output[@]}; do
        python3 tabular.py $file
    done

elif [[ "$#" = 4 ]]; then
    python3 reducer.py $1 $2 $3
    output=`find ./OUTPUT/${1}/ -name '*.json'`

    for file in ${output[@]}; do
        python3 tabular.py $file
    done
    
else
    echo -n "Ack! Invalid user input"
fi
