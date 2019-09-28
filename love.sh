#!/bin/sh
python creds.py
echo "This script is about to run another script."
sh ./test.sh.sh
echo "This script has just run another script."

