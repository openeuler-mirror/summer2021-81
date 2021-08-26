if [[ -z "$(grep -w mockbuild /etc/passwd)" ]];then
    printf create user mockbuild, please input root passwd
    sudo useradd mockbuild
fi

if [[ -z "$(grep -w mock /etc/group)" ]];then
    printf create group mock, please input root passwd
    sudo groupadd mock
fi

find . -name "*src.rpm" | xargs rpm -i
