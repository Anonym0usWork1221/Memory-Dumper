#!/bin/bash

if [[ "$(uname)" == "Linux" ]]; then
    # Linux platform
    echo "Detected Linux platform."
    sudo apt install cmake -y
    pip3 install .
elif [[ "$(uname)" == "Android" ]]; then
    # Android platform
    echo "Detected Android platform."
    pkg update && pkg upgrade
    pkg install cmake -y
    pkg install tsu -y
    pkg install python3 -y
    pip3 install .
else
    echo "Unsupported platform."
fi
