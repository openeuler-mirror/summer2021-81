#!/bin/sh
for line in $(cat ./builddep_vlc); do
    dnf provides $line > ./tmp
    str=$(sed -n 2p ./tmp)
    echo ${str%:*} >> ./vlc_deplist
done
