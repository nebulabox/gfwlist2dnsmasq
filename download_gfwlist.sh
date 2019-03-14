#!/usr/bin/env bash
aria2c https://github.com/gfwlist/gfwlist/raw/master/gfwlist.txt
base64 -d ./gfwlist.txt > gfwlist_out.txt
rm ./gfwlist.txt
