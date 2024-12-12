#!/bin/bash

if [ "$#" -ne 4 ]; then
  echo "Usage: $0 <PATH> <APPLICATION> <DEVICE> <SCENARIO_NAME>"
  exit 1
fi

FOLDER_PATH=$1
APPLICATION=$2
DEVICE=$3
SCENARIO_NAME=$4  

# Search all files 'recording.mp4'
NAME='*'$APPLICATION'*'$SCENARIO_NAME'*recording.mp4'

NAME_ENCODED='*'$APPLICATION'*'$SCENARIO_NAME'*recording-encoded.mp4'
#find $FOLDER_PATH -type f -name $NAME

for file in `ls -R $FOLDER_PATH/*/$NAME`; do
    echo "-" $file
    file_encoded=$(echo $file | sed -e 's/recording/recording-encoded/g')
    file_name=$(basename $file)
    file_encoded_name=$(basename $file_encoded)
    file_latency_name=$file_encoded_name"-latencies.csv"
    file_csv_name="/tmp/$file_encoded_name-latencies.csv"
    file_server_path=$(dirname "$file") 

    if [ -f $file_server_path"/"$file_latency_name ];then
        echo "The latency was meassured"
        echo "-----"
        continue
    fi

    # if [ -f $file_encoded ];then
    #     echo "$file_encoded was encoded"
    #     # Copy the file to local path before the analysis
    #     echo "cp $file_encoded /tmp/$file_encoded_name"
    #     cp $file_encoded /tmp/$file_encoded_name
    # else 
        echo "$file_encoded not was encoded"
        # Copy the original file to local path before encoding
        echo "cp $file /tmp/$file_name"
        cp $file /tmp/$file_name
        
        echo "run ffmpeg"
        ffmpeg -i /tmp/$file_name -vf "fps=30" -vsync vfr -c:v libx264 -preset medium -crf 23 -c:a copy /tmp/$file_encoded_name -y
    #fi


    # Meassure the latency
    #/usr/local/anaconda3/envs/igperformance/bin/python track_latency.py /tmp/$file_encoded_name $APPLICATION $SCENARIO_NAME
    python3.10 track_latency.py /tmp/$file_encoded_name $APPLICATION $SCENARIO_NAME
    
    # copy results to folder 
    
    cp $file_csv_name $file_server_path


    echo "Removing /tmp/...."
    # Remove /tmp file
    rm /tmp/$file_name
    rm /tmp/$file_encoded_name
    rm $file_csv_name

    echo "-----"

    
done