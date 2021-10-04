#!/bin/bash
up=~/upload
mkdir -p $up
tot=$(find . -name "*.src.rpm" | wc -l)
cnt=0
for file in *.src.rpm; do
    name=${file%%-[0-9]*}
    dir=$up/$name
    mkdir -p "$dir"
    cp "$file" "$dir"
    pushd "$dir"
    rpm2cpio "$file" | cpio -idmv
    rm "$file"
    popd
    cnt=$((cnt+1))
    num=$(echo "scale=2; $cnt / $tot * 100" | bc)
    echo "processed $num %" 
done
