#!/bin/bash
todo=./upload.list
if [[ "$(whoami)" == "root" ]]; then
    echo please run in normal user! not root!!!
    exit 1
fi

while read -r name; do
    [[ ! -d $name ]] && echo "$name dir doesn't exist" && continue
    pushd $name
    url_name=$(echo "$name" | tr "A-Z" "a-z")
    if [[ ! -d .git ]];then
        git init -b master
        git remote add origin https://gitee.com/retropie-rpms/"$url_name".git
        git add .
        git commit -m "init $name"
    else
        git remote set-url origin https://gitee.com/retropie-rpms/"$url_name".git
        git add .
        git commit -m "init $name"
    fi
    git push --set-upstream origin master
    popd
done < $todo