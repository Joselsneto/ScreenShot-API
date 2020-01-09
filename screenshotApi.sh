#!/bin/sh

PROJECTPATH="/home/jose/Projects/malware-patrol/ScreenShot-API"

case $1 in
    start_debug)
        echo "Starting screenshot API in debug mode"
        $PROJECTPATH/src/deleteScreenshots.sh &
        python3 index.py &
        ;;
    start)
        # Change to production mode
        echo "Starting screenshot API"
        $PROJECTPATH/src/deleteScreenshots.sh &
        python3 index.py &
        ;;
    generate_key)
        NEW_UUID=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
        echo $NEW_UUID
        echo $NEW_UUID >> authorized_keys
        ;;
    install)
        mkdir -p temp/screenshots
        pip3 install flask
        pip3 install flask-restful
        pip3 install flask-jsonpify

        ;;
    stop)
        echo "Stoping screenshot API"
        kill $(pgrep -f "/bin/sh ${PROJECTPATH}/src/deleteScreenshots.sh")
        kill $(pgrep -f 'python3 index.py')
        ;;
    *)
        echo "Usage: ./screenshotApi.sh {start_debug | start | generate_key | install}"
        ;;
esac

exit 0