#!/bin/bash
# Bash script thattakes in URL as an argument,and displays body of the response
curl - s "$1" - H "X-School-User-Id: 98"
