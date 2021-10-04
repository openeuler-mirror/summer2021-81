#!/bin/bash
todo=./todo.list
for name in $(cat $todo); do
    file=~/rpmbuild/SPECS/$name.spec
    if [[ -f $file ]]; then
        printf "$name " 
        cat $file | grep License
    else
        printf "### couldn't find $file ###\n"
    fi
done