#!/bin/bash

out_dir=~/upload_info
mkdir -p $out_dir

src_out=$out_dir/src-Retropie.yaml
sig_out=$out_dir/sig.yaml
exist=$out_dir/exist_package

[[ -f $src_out ]] && rm $src_out
[[ -f $sig_out ]] && rm $sig_out
[[ -f $exist ]] && rm $exist

cd ~/upload
for name in *; do
  grep -x "  - src-openeuler/$name" ~/community/sig/sigs.yaml
  find=$?
  if [[ "$find" == "0" ]]; then
    echo $name >> $exist
    printf "in sigs.yaml:     %s exist \n\n" "$name"
    continue
  fi
  pushd $name >/dev/null 2>&1

  small_name=$(echo "$name" | tr "A-Z" "a-z")
  
  spec=$(find . -name "*.spec")
  description=$(rpmspec -q --qf "%{Summary}\n" $spec 2>/dev/null | head -n 1 )
  upstream=$(rpmspec -q --qf "%{url}\n" $spec 2>/dev/null | head -n 1 )

  yaml="- name: $small_name
  description: $description
  upstream: $upstream
  branches:
  - name: master
    type: protected
  type: public"
  echo -e "$yaml" >> $src_out

  echo "  - src-openeuler/$small_name" >> $sig_out
  popd >/dev/null 2>&1
done