#!/bin/bash -x
up_dir=~/upload
if [[ "$(whoami)" == "root" ]]; then
    echo "please run in normal user! not root!"
    exit 1
fi

if [[ ! -d $up_dir ]]; then
    echo "$up_dir doesn't exit !"
    exit 1
fi

pushd $up_dir

for name in *; do
    pushd $name
    url_name=$(echo "$name" | tr "A-Z" "a-z")

    description=$(cat *.spec | grep Summary | head -n 1)
    description=$(echo ${description#*: })  # cut strings before ": " 

    echo $url_name
    echo $description

    read
    
    url="'https://gitee.com/api/v5/orgs/Retropie-rpms/repos'"
    query={\"access_token\":\"\",\"name\":\"$url_name\",\"description\":\""$description"\",\"has_issues\":\"true\",\"has_wiki\":\"true\",\"can_comment\":\"true\",\"public\":1,\"private\":\"false\",\"path\":\"test\"}

    curl -X POST --header 'Content-Type: application/json;charset=UTF-8' $url -d $query

    [[ "$?" != "0" ]] && echo create repo fail! && exit 1

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
done

popd