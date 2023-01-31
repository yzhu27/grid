'''
---                            __     
---                    __     /\ \    
---     __      _ __  /\_\    \_\ \   
---   /'_ `\   /\`'__\\/\ \   /'_` \  
---  /\ \L\ \  \ \ \/  \ \ \ /\ \L\ \ 
---  \ \____ \  \ \_\   \ \_\\ \___,_\
---   \/___L\ \  \/_/    \/_/ \/__,_ /
---     /\____/                       
---     \_/__/                        
'''

import math
import re
import sys
import csv



the = {}
help = """
gird.lua : a rep grid processor
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 

USAGE: grid.lua  [OPTIONS] [-g ACTION]

OPTIONS:
  -d  --dump    on crash, dump stack   = false
  -f  --file    name of file           = ../etc/data/repgrid1.csv
  -g  --go      start-up action        = data
  -h  --help    show help              = false
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211

ACTIONS:
"""

