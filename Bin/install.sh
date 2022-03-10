#!/bin/bash
GROUP_FILE="/etc/sudoers.d/web_manager"
group_name="web_manager"
GROUPS_NAME=`cat /etc/group | awk -F ':' '{print $1}'`

function _install(){
	SCRIPT=$(readlink -f "$0")
	SCRIPTPATH=$(dirname $(dirname $(dirname "$SCRIPT")))
	cd -P $SCRIPTPATH
	
	echo $SCRIPTPATH
}
if [[ $UID -gt 0 ]];then
	echo "Only root can run this script."
	exit 1
fi
if [[ -f $GROUP_FILE ]];then
	echo 'File exist'
	_install
else
	for i in $GROUPS_NAME
	do
		if [ "$i" == "$group_name" ];then
			group_exist="$i"
		else
			group_exist=""
		fi
	done
	if [ "$group_exist" == "$group_name" ];then
		echo -e 'This file created by Ansible_webManager \n%web_manager   ALL=(ALL)   ALL' > $GROUP_FILE
		echo "File Created!!"
	else
		echo -e "The group named 'web_manager' not created!!\nCreating ..."
		sudo groupadd "$group_name"
	fi
	_install
fi