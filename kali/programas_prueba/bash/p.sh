#!/bin/bash
for port in $(seq 1 65535); do
	a=$((($port / 65535)*100))
	g=65535
	c=$(echo "scale=2; ($port/$65535)*100" | bc)
	echo "$a $port $c"
done; wait
