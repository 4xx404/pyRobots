#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time
from modules.stylesheet import bc, sd, menu
from modules.quickScan import quick
banner = sd.banner.logo
help = menu.helper
eBan = sd.eBan
iBan = sd.iBan
sBan = sd.sBan

try:
	os.mkdir('Pulled-Data')
except FileExistsError:
	pass
except Exception:
	os.system('clear')
	print(banner)
	print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Failed to create ' + bc.RC + '/Pulled-Data/' + bc.BC + ' Directory\n')
	quit()

os.system('clear')
print(banner)
print(help)

def robotMenu():
	try:
		host = str(input(bc.BC + " URL: " + bc.GC))
		if(host == ''):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'URL value cannot be empty\n')
			quick()			
		elif(host.startswith('http://') or host.startswith('https://')):
			if(host.endswith('/')):
				host = host
			else:
				host = host + '/'
			quick(host)
		else:
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid URL value\n')
			quick()
	except ValueError:
		os.system('clear')
		print(banner)
		print(menu)
		print(eBan + bc.RC + "ERROR: " + bc.BC + 'Value must be INTEGER [' + bc.GC + '0-3' + bc.BC + ']\n')
		robotMenu()
	except KeyboardInterrupt:
		os.system('clear')
		print(banner)
		print(bc.BC + ' Clearing Cache...')
		os.system('rm -rf modules/__pycache__/')
		time.sleep(0.5)
		os.system('clear')
		print(banner)
		quit()
if __name__ == '__main__':
	robotMenu()
