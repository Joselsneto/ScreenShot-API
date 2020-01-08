#!/bin/sh

case $1 in
    start_debug)
        echo "Starting screenshot API in debug mode"
        ./src/deleteScreenshots.sh &
        python3 index.py &
        ;;
    start)
        # Change to production mode
        echo "Starting screenshot API"
        ./src/deleteScreenshots.sh &
        python3 index.py &
        ;;
    generate_key)
        NEW_UUID=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
        echo $NEW_UUID
        echo $NEW_UUID >> authorized_keys
        ;;
    install)
        mkdir -p temp/screenshot
        pip3 install subprocess
        pip3 install flask
        pip3 install flask-restful
        pip3 install flask-jsonpify
        ;;
    stop)
        echo "Stoping screenshot API"
        kill $(pgrep -f '/bin/sh ./src/deleteScreenshots.sh')
        kill $(pgrep -f 'python3 index.py')
        ;;
    *)
        echo "Usage: ./screenshotApi.sh {start_debug | start | generate_key}"
        ;;
esac

exit 0