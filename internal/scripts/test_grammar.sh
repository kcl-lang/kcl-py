#!/usr/bin/env bash

# Environment
if [ -f "/etc/os-release" ]; then
    source /etc/os-release
    os=$ID
else
    os=$(uname)
fi
src="$(realpath $(dirname $0))/../../"
topdir=$(realpath $(dirname $0)/../../)
kclvm_source_dir="$topdir"

# Grammar test
cd $kclvm_source_dir/test/grammar
python3 -m pip install -r ${src}/kclvm/scripts/requirements.txt
python3 -m pip install --upgrade pip
python3 -m pip install pytest pytest-xdist
python3 -m pytest -vv -n 10
