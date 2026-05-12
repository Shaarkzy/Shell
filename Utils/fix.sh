#!/bin/bash

if [[ "$(uname -a | grep -i android)" ]]; then
	#do  nothing for android
    echo "hello"

else
    #do nothing for debian
    echo "hello test"
fi
