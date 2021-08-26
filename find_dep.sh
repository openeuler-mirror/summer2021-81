times=6
next=$((times+1))
echo "" > deplist_$next
echo "" > details
for spec in $(cat fail.log); do
    dnf builddep ~/rpmbuild/SPECS/$spec -y &> /dev/null
    if [[ "$?" != "0" ]]; then
        echo $spec:
        dnf builddep ~/rpmbuild/SPECS/$spec 2>&1 1>/dev/null | grep "No matching" | awk -F \' '{ print $2 }'
        echo ""
    fi
done
