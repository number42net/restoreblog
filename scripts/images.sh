#!/bin/bash
c=$(ls img_???.* 2>/dev/null | tail -1 | cut -c 5-7)

if [ -z "$c" ]; then
    c=0
fi

for i in $(ls *.jpg *.png 2> /dev/null| grep -v "img_..."); do 
    c=$((c+1))
    mv $i img_$(printf "%03d\n" $c).$(echo $i | awk -F. '{print $2}')
done

for i in $(ls *.jpg *.png 2> /dev/null); do 
    if [ ! -f ../$i ]; then 
        echo $i
        convert $i -auto-orient -strip $i
        convert $i -resize 1024x800\> ../$i
    fi
done