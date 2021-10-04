#!/bin/bash
not_vlc=("fbset libboost-filesystem libgles2-mesa libraspberrypi fbida fcitx game-music-emu libcec intel-mediasdk libvncserver id3lib imsettings ocl-icd platform sysconftool libgxim")

vlc_out=vlc.yaml
sig_out=sig.yaml
log=attention.log
rm $vlc_out
rm $sig_out
rm $log
tmp=$(mktemp)
for spec in $(ls ~/rpmbuild/SPECS); do
    name=${spec%.*}
    printf "processing $name ...\n"

    echo "${not_vlc}" | grep $name
    find=$?
    if [[ "$find" == "0" ]]; then
        printf "$name is not a vlc dependency, we don't need it"
        continue    # we don't need these packages from not_vlc
    fi

    sudo dnf info $name > $tmp
    rc=$?
    if [[ "$rc" != "0" ]]; then
      # we can't find it from repo,so we find it from spec
      # attention, I don't eval the macros in spec,so this may cause some porblems, you should check the yamls
      printf "#### attention! find $name info in its spec files  #### \n"
      echo $name >> $log
      info=~/rpmbuild/SPECS/$spec
    else
      info=$tmp
    fi
    description=$(cat $info | grep Summary | head -n 1)
    description=$(echo ${description#*: })  # cut strings before ": " 

    upstream=$(cat $info | grep URL | head -n 1)
    upstream=$(echo ${upstream#*: })  # cut strings before ": " 

    yaml="- name: $name
  description: $description
  upstream: $upstream
  branches:
  - name: master
    type: protected
  type: public"
    echo -e "$yaml" >> $vlc_out

    echo "  - src-openeuler/$name" >> $sig_out
done
rm $tmp