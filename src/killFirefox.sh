#!/bin/sh

while :
do
    PID=0
    PID=`ps -eo comm,pid,etimes | awk '/^firefox/ {if($3 > 60) {print $2}}'`
    if [ "$PID" != "" ] 
    then
        kill -9 $PID
        echo "$PID killed"
    fi
    sleep 1
done