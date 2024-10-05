#!/bin/bash

gawk -F, '$3 == 2 && $NF ~ /S/' hw4/titanic.csv | sed 's/female/F/g' | sed 's/male/M/g' | gawk -F, '{
    if($(NF-6) != null ) {
        sum += $(NF-6);
        count++;
    }
    print $0;
} END {
    print "Average age is " sum / count;
}'