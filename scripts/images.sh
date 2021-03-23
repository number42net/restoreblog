#!/bin/bash
for i in $(ls *.jpg *png 2> /dev/null); do 
    if [ ! -f ../$i ]; then 
        echo $i
        convert $i -auto-orient -strip $i
        convert $i -resize 1024x800\> ../$i
    fi
done