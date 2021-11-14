#! /bin/bash

if type -t wevtutil &> /dev/null
then
	OS=MSWin
elif type -t scutil &> /dev/null
then
	OS=macOS
else
	OS=Linux
fi
echo $OS

#!/bin/bash 

function is_alive_ping() { 

  ping -c 1 $1 > /dev/null 2>&1 

  [ $? -eq 0 ] && echo "Node with IP: $i is up."
  for ((counter=10; counter<=500; counter++)) 

do 

    (echo >/dev/tcp/$i/$counter) > /dev/null 2>&1 && echo "$counter open" 

done 

} 

for i in 192.168.100.{1..255} 

do 

  is_alive_ping $i & disown 

done 

