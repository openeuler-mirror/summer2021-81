#!/bin/sh
for rpm in $(cat vlc_deplist); do
    dnf download --source $rpm --destdir ./dep_rpm
done