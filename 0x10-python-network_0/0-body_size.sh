#!/usr/bin/python3
# Displays body size of URL
size=$(curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r\n')