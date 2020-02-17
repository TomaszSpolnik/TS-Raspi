#!/bin/bash

while true

do vcgencmd get_mem arm && vcgencmd get_mem gpu >> memory_usage.txt
sleep 7200

done &
