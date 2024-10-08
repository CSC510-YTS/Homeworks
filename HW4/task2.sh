#!/bin/bash

grep -r -l 'sample' dataset1/ | xargs grep -c 'CSC510' | grep -P -v ':[012]$' | gawk -F: '{ "ls -l "$1"" |& getline fileDetails; print fileDetails, $2}' | sort -k10,10nr -k5,5nr | cut -d ' ' -f10 | sed 's\'hw4/dataset1/file_'\filtered_\'
