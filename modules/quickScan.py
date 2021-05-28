#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time
import requests
import random
import wget
from modules.stylesheet import bc, sd
banner = sd.banner.logo
eBan = sd.eBan
iBan = sd.iBan
sBan = sd.sBan
scanType = sd.quick
headers = {'Accept-Language': 'en-US,en;q=0.5', 'Cache-Control': 'no-cache', 'User-Agent': 'pyRobots.V2'}

os.system('clear')
print(banner)
print(scanType)

def quick(host):
	try:	
		url = host + 'robots.txt'
		req = requests.get(url, headers=headers)
		if(req.status_code == 200):
			print(sBan + ' Host: ' + bc.GC + host + bc.BC + ' includes robots.txt file\n')

			os.chdir('Pulled-Data')
			key = random.randrange(0, 99999999)
			try:
				setKey = str(key)
				os.mkdir(setKey)
			except FileExistsError:
				pass
			except Exception:
				os.system('clear')
				print(banner)
				print(eBan + " Failed to create " + setKey + " Directory\n")
				quick(host)

			os.chdir(setKey)
			time.sleep(0.5)
			print(bc.BC + " Starting Download for robots.txt...\n")
			try:
				wget.download(url)
			except Exception:
				os.system('clear')
				print(banner)
				print(scanType)
				print(eBan + " Failed to Download: " + bc.GC + url + "\n")
				quick(host)

			os.system('clear')
			print(banner)
			print(scanType)
			try:
				robotsTxt = open('robots.txt', 'r')
				lines = robotsTxt.readlines()
			except Exception:
				os.system('clear')
				print(banner)
				print(scanType)
				print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Failed to load robots.txt\n')
				quick(host)

			print(iBan + " Loading robots.txt for Host: " + bc.GC + host)
			time.sleep(0.5)
			files = []
			x = open('directories.txt', 'a+')
			for line in lines:
				if(line.startswith('Disallow: ')):
					line = line.replace('Disallow: /', '').replace('Disallow: ', '').replace('\n', '')
					if(line.endswith('/')):
						x.write(line + '\n')
					else:
						file = host + line[0:]
						os.system('clear')
						print(banner)
						print(scanType)
						print(bc.BC + ' Trying to download: ' + bc.GC + file)
						try:
							wget.download(file)
							files.append(file)
							time.sleep(0.5)
						except Exception:
							continue
				else:
					continue

			x.close()
			
			os.system('clear')
			print(banner)
			print(scanType + '\n')
			print(sBan + ' ['+bc.GC +'DOWNLOADED' + bc.BC + '] robots.txt results:')
			fileCount = 0
			for file in files:
				fileCount += 1
				print(bc.BC + "\t" + bc.GC + '/' + file.replace(host, ''))
			if(fileCount == 1):
				fPlace = 'file'
			else:
				fPlace = 'files'
			
			print('\n' + sBan + ' Scan Complete for Host: ' + bc.GC + host)
			print(sBan + ' Downloaded Disallowed Entries: ' + bc.GC + str(fileCount) + ' ' + fPlace)
			print(sBan + ' Useful data may have been downloaded to ' + bc.GC + '/Pulled-Data/' + setKey + '/\n')

			dirChoice = str(input(sd.extendedChoiceBanner)).lower()
			if(dirChoice == 'y'):
				from modules.directoryScan import extended
				extended(host, setKey)
			else:
				os.system('rm -rf modules/__pycache__/ ../../modules/__pycache__/')
				from pyRobots import robotMenu
				robotMenu()
		else:
			os.system('clear')
			print(banner)
			print(scanType)
			print(eBan + ' Host: ' + bc.GC + host.replace(robots, '') + bc.BC + ' does not include robots.txt file\n')
			quick(host)

	except KeyboardInterrupt:
		os.system('clear')
		print(banner)
		print(scanType + '\n')
		print(sBan + ' ['+bc.GC +'DOWNLOADED' + bc.BC + '] robots.txt results:')
		fileCount = 0
		for file in files:
			fileCount += 1
			print(bc.BC + "\t" + bc.GC + '/' + file.replace(host, ''))
		
		if(fileCount == 1):
			fPlace = 'file'
		else:
			fPlace = 'files'
		print('\n' + sBan + ' Scan Complete for Host: ' + bc.GC + host)
		print(sBan + ' Downloaded Disallowed Entries: ' + bc.GC + str(fileCount) + ' ' + fPlace)
		print(sBan + ' Useful data may have been downloaded to ' + bc.GC + '/Pulled-Data/' + setKey + '/\n')
		os.system('rm -rf modules/__pycache__/ ../../modules/__pycache__/')
		quit()
