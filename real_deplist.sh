#!/bin/sh -x
times=7
touch ./deplist_$times
for i in $(cat ../deplist_$times); do
    grep_res=$(grep $i ./deplist*)
    if [[ -z "$grep_res" ]];then
        echo $i >> ./deplist_$times
    fi
done