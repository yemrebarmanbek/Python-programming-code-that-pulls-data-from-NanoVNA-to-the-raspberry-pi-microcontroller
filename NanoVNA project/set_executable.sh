#!/bin/sh
# you might want to change the directory below into the targeted directory
DIR="/home/pi/progetto/nanovna_data"
inotifywait -m -r -e move -e create --format '%w%f' "$DIR" | while read f

do
  python NanoVNA_prediction.py
done