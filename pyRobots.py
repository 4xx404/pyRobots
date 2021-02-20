#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time
from quickScan import quick
from extendedScan import extensive
from advancedScan import advanced

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

os.system('clear')
print(banner)

def robotMenu():
	print(bc.BC + ' 1. ' + bc.GC + 'Quick Scan' + bc.BC + '\t\t\tScan Speed: ' + bc.GC + 'Fast')
	print(bc.BC + ' 2. ' + bc.GC + 'Entended Scan' + bc.BC + '\t\tScan Speed: ' + bc.BC + 'Slow')
	print(bc.BC + ' 3. ' + bc.GC + 'Advanced Scan' + bc.BC + '\t\tScan Speed: ' + bc.RC + 'Very Slow\n')

	try:
		menu = int(input(bc.BC + ' Option: ' + bc.GC))	
		if menu == 1:
			os.system('clear')
			print(banner)
			quick()
			
		elif menu == 2:
			os.system('clear')
			print(banner)
			extensive()
			
		elif menu == 3:
			os.system('clear')
			print(banner)
			advanced()

		elif menu == 0:
			print(bc.BC + ' Closing pyRobots...')
			time.sleep(1)
			quit()
	
		else:
			os.system('clear')
			print(banner)
			print(errorBanner + bc.RC + "ERROR: " + bc.BC + "Invalid Option" + errorBanner)
			robotMenu()

	except Exception:
		os.system('clear')
		print(banner)
		print(errorBanner + bc.RC + "ERROR: " + bc.BC + "Invalid Option" + errorBanner)
		robotMenu()

	except KeyboardInterrupt:
		os.system('clear')
		print(banner)
		print(bc.BC + ' Clearing Cache...')
		os.system('rm -rf __pycache__/')
		time.sleep(1)
		print(bc.BC + ' Closing pyRobots...')
		time.sleep(1)
		quit()

if __name__ == '__main__':
	robotMenu()
