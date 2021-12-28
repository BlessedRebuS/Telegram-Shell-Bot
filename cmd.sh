#!/bin/bash

res=""

for var in "$@"
do
    res+=" "$var
done

echo $res

$res &> cmd.txt