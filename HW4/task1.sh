#!/bin/bash

kill  $(ps aux | grep 'bash infinite.sh' | grep -v grep |awk '{print $2}')
