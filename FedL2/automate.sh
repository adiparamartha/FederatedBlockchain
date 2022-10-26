#!/bin/bash

echo "This is brownie using shell script"  
for i in {1..50}
do
   brownie run scripts/store.py &
   # sleep 1
done
wait

