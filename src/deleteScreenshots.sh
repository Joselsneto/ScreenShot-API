#!/bin/sh

while :
do
    find ../temp/screenshots -mmin +1 -type f -exec rm -fv {} \;
    sleep 10
done