#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time
import requests
import random

class bc:
	GC = '\033[1;39m'
	BC = '\033[1;34m'
	RC = '\033[1;31m'

banner = bc.RC + '''
               ___       __        __     
    ___  __ __/ _ \___  / /  ___  / /____ 
   / _ \/ // / , _/ _ \/ _ \/ _ \/ __(_-< 
  / .__/\_, /_/|_|\___/_.__/\___/\__/___/ 
 /_/   /___/                              
'''

infoBanner = bc.BC + " [" + bc.GC + "?" + bc.BC + "]"
successBanner = bc.BC + " [" + bc.GC + "*" + bc.BC + "]"
errorBanner = bc.BC + " [" + bc.RC + "!" + bc.BC + "]"
scanType = bc.BC + ' Scan Type: ' + bc.GC + 'Extended Scan\t\t' + bc.BC + 'Scan Speed: Slow\n'

os.system('clear')
print(banner)

def extensive():
	print(scanType)
	print(infoBanner + " Enter " + bc.GC + "#//" + bc.BC + " to return to the main menu" + infoBanner)
	print('\n' + infoBanner + " Extended Scan feature build is in progress..." + infoBanner)

	try:
		host = str(input(bc.BC + " URL: " + bc.GC))
		if host == '#//':
			os.system('clear')
			os.system(banner)
			from pyRobots import robotMenu
			robotMenu()

		else:
			os.system('clear')
			print(banner)
			print(scanType)
			print(infoBanner + " Extended Scan feature build is in progress..." + infoBanner)
			input(bc.BC + ' Press Enter to Continue...')
			os.system('clear')
			print(banner)
			extensive()

	except KeyboardInterrupt:
		os.system('clear')
		print(banner)
		print(scanType)
		print(bc.BC + ' Clearing Cache...')
		os.system('rm -rf __pycache__/')
		time.sleep(1)
		print(bc.BC + ' Closing pyRobots...')
		time.sleep(1)
		quit()
