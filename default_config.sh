#!/bin/bash

config_single(){
	echo "dev s${1}-eth${2} are going to be configured"
	tc qdisc delete dev s${1}-eth${2} root
	tc qdisc add dev s${1}-eth${2} handle 1: root dsmark indices 1 default_index 0
	tc qdisc add dev s${1}-eth${2} handle 2: parent 1: tbf burst 2048KB latency ${3} mtu 1514 rate ${4}Gbit
	tc qdisc show dev s${1}-eth${2}
}

#configure ports of layer 1
for i in $( seq 1 9 )
do
	config_single "30${i}" 1 75000 1
done
for i in $( seq 10 20 )
do
	config_single "3${i}" 1 75000 1
done
#configure ports of layer 2
for i in $( seq 1 2 )
do
	config_single "20${i}" 1 75000 9.5
done
#configure ports of layer 3
config_single "101" ${i} 75000 18.5