#!/bin/sh
ls
pwd
whoami
cd $WORKSPACE
git clone -b test git@github.com:rama2027/love.git
cd love
pwd
python EC2creation.py
echo "This script is about to run another script."
sh ./test.sh
echo "This script has just run another script."

