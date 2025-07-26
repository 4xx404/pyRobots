#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

sys.dont_write_bytecode = True

class bc:
	GC = "\033[1;39m"
	BC = "\033[1;34m"
	RC = "\033[1;31m"
	
class sd:
	iBan = f"{bc.BC}[{bc.GC}?{bc.BC}]" # Info banner
	sBan = f"{bc.BC}[{bc.GC}" + u'\u2713' + f"{bc.BC}]" # Success banner
	eBan = f"{bc.BC}[{bc.RC}" + u'\u2717' + f"{bc.BC}]" # Error banner
	
class Banner:
	Author = f"{bc.BC}\n Author:{bc.GC} 4xx404 \n"
	Version = f"{bc.BC} Version:{bc.GC} 1.0 \n"
	Github = f"{bc.BC} Github: {bc.GC}https://github.com/4xx404 \n"

	Logo = rf"""{bc.RC}
                       ___       __        __     
	{bc.GC}    ___  __ __/ _ \___  / /  ___  / /____ 
	{bc.BC}   / _ \/ // / , _/ _ \/ _ \/ _ \/ __(_-< 
	{bc.RC}  / .__/\_, /_/|_|\___/_.__/\___/\__/___/ 
	{bc.GC} /_/   /___/                              
	{Author}{Version}{Github}"""

class Menu:
	Helper = f"{sd.iBan} Include {bc.GC}http://{bc.BC} | {bc.GC}https://{bc.BC} in URL"