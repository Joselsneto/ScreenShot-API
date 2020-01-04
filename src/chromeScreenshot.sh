#!/bin/sh

google-chrome --headless --disable-gpu --screenshot=../temp/screenshot/$1.$2 --window-size=$3,$4 --default-background-color=0 $5 