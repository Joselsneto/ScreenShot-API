#!/bin/sh
# Delete all files in temp/screenshots that are older than 1 minute

while :
do
    find $1 -mmin +1 -type f -name "mps_*.png" -exec rm -fv {} \;
    find $1 -mmin +1 -type f -name "mps_*.jpg" -exec rm -fv {} \;
    find $1 -mmin +1 -type f -name "mps_*.jpeg" -exec rm -fv {} \;
    sleep 10
done