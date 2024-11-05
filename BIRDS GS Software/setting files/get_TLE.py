#!/usr/bin/env python3
# get_TLE.py : get latest TLE from celestrak

import urllib.request

sourceURL = "http://celestrak.org/NORAD/elements/stations.txt"
nameList = ["ISS (ZARYA)", "KITSUNE", "FUTABA"]

with urllib.request.urlopen(sourceURL) as f:
    obj = f
    str = obj.read().decode("cp932")
    lines = str.split("\n")
    
    for i, line in enumerate(lines):
        for name in nameList:
            if(name in line):
                print(lines[i].strip())
                print(lines[i+1].strip())
                print(lines[i+2].strip())
