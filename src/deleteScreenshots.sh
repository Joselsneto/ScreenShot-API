#!/bin/sh
# Delete all files in temp/screenshots that are older than 1 minute

while :
do
    find ./temp/screenshots -mmin +1 -type f -exec rm -fv {} \;
    sleep 10
done