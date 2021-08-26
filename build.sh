#!/bin/sh
times=$1
todo_dir=dep_rpm_$times
rpms=$todo_dir.tar.gz
fail_log=~/vlc/fail_$times.log
done_dir=~/vlc/done_$times
if [[ ! -e $rpms ]]; then
    cp ~/share/$rpms .
    tar xf $rpms
fi

rm -rf ~/rpmbuild/{SPECS,SRPMS}
for rpm in $(ls $todo_dir); do
    rpm -i ./$todo_dir/$rpm
done

if [[ -e $fail_log ]]; then
    rm $fail_log
fi
mkdir -p $done_dir

cd ~/rpmbuild/SPECS/
for spec in $(ls .); do
    good=1
    if [[ -n "$(ls ~/vlc/done_$times | grep $spec)" ]]; then
        cp $spec $done_dir
    fi

    name=${spec%.*}
    
    if [[ -z "$(ls ~/rpmbuild/RPMS/*/ | grep $name)" ]]; then 
        sudo dnf builddep --spec $spec -y
        rpmbuild -ba $spec
        if [[ "$?" != "0" ]]; then
            good=0
        fi
    fi

    if [[ "$good" == "0" ]]; then
        echo $spec >> $fail_log
    else
        cp $spec $done_dir
        sudo dnf in ~/rpmbuild/RPMS/*/* --skip-broken -y
    fi
done
