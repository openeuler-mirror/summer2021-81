#!/bin/bash
$name=$1
$description=$2

curl -X POST --header 'Content-Type: application/json;charset=UTF-8' 'https://gitee.com/api/v5/orgs/Retropie-rpms/repos' -d '{"access_token":"这里填你的token","name":"test","description":"my description","has_issues":"true","has_wiki":"true","can_comment":"true","public":1,"private":"false","path":"test"}'