#!/bin/sh
times=$1
name=dep_rpm_$times
rpms=$name.tar.gz
if [[ ! -e $rpms ]]; then
    cp ~/share/$rpms .
    tar xf $rpms
fi

rm -rf ~/rpmbuild/{SPECS,SRPMS}
for rpm in $(ls $name); do
    rpm -i ./$name/$rpm
done

cd ~/rpmbuild/SPECS/
rm ~/vlc/fail_$times.log
mkdir -p ~/vlc/done_$times
for spec in $(ls .); do
    name=${spec%.*}
    if [[ -z "$(ls ~/rpmbuild/RPMS/*/ | grep $name)" ]]; then 
        sudo dnf builddep --spec $spec -y
        rpmbuild -ba $spec
        if [[ "$?" != "0" ]]; then
            echo $spec >> ~/vlc/fail_$times.log
        else
            cp $spec ~/vlc/done_$times
            sudo dnf in ~/rpmbuild/RPMS/*/* --skip-broken -y
        fi
    else
        cp $spec ~/vlc/done_$times
    fi
done
