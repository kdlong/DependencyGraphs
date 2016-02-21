#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "requires 1 command line arguments: test.sh <cmssw_config_file>"
    exit
fi
cmsRun $1 2>&1  | grep "may consume" >& test.dat
python test.py
dot graphtest.gv -Tps > ~/www/test.ps
dot graphtest.gv -Tpng > ~/www/test.png
