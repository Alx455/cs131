#!/bin/bash

MAKE=$1
shift
MODEL="$*"

awk -F, -v make="$MAKE" -v model="$MODEL" 'BEGIN {sum=0; count=0} {if ($2 == make && $3 == model && $10 != 1) {sum+=$15; count++}} END{if (count > 0) print "Average cost of used", make, model, ": ", sum/count}' car_prices.csv
