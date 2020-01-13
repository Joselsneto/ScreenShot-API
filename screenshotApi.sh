#!/bin/sh

PROJECT_PATH="/home/jose/Projects/malware-patrol/ScreenShot-API"
SCREENSHOT_PATH="/home/jose/Projects/malware-patrol/ScreenShot-API/temp/screenshots"
KEYS_PATH="/home/jose/Projects/malware-patrol/ScreenShot-API"

case $1 in
    start_debug)
        echo "Starting screenshot API in debug mode"
        $PROJECT_PATH/src/deleteScreenshots.sh $SCREENSHOT_PATH &
        python3 index.py &
        ;;
    start)
        # Change to production mode
        echo "Starting screenshot API"
        $PROJECT_PATH/src/deleteScreenshots.sh $SCREENSHOT_PATH &
        python3 index.py &
        ;;
    generate_key)
        NEW_UUID=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
        echo $NEW_UUID
        echo $NEW_UUID >> $KEYS_PATH/authorized_keys
        ;;
    install)
        mkdir -p $SCREENSHOT_PATH
        pip3 install flask
        pip3 install flask-restful
        pip3 install flask-jsonpify
        ;;
    stop)
        echo "Stoping screenshot API"
        kill $(pgrep -f "/bin/sh ${PROJECT_PATH}/src/deleteScreenshots.sh")
        kill $(pgrep -f 'python3 index.py')
        ;;
    *)
        echo "Usage: ./screenshotApi.sh {start_debug | start | generate_key | install}"
        ;;
esac

exit 0