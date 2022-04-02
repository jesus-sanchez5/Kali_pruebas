#!/bin/bash
if [ $1 ]; then
	ip_address=$1
	for port in $(seq 1 65535); do
		a=$((($port / 65535) *100))

	#	timeout 1 bash -c "echo '' > /dev/tcp/$ip_address/$port" 2>/dev/null && echo "[*] Puerto $port open $a%" &
	echo "$a $port"
	done; wait
else
	echo -e "\n [*] Uso: ./scan.sh <ip-address>\n"
	exit 1
fi
