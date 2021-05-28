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
scanType = sd.extended
headers = {'Accept-Language': 'en-US,en;q=0.5', 'Cache-Control': 'no-cache', 'User-Agent': 'pyRobots.V2'}

os.system('clear')
print(banner)
print(scanType)

def extended(host, setKey):
	try:
		x = open('directories.txt', 'r')
		dirs = x.readlines()
	except Exception:
		os.system('clear')
		print(banner)
		print(scanType)
		print(eBan + bc.RC + ' ERROR: ' + 'Failed to open directory file\n')
		extended()
	
	directories = []
	for _dir in dirs:
		if(_dir.startswith('/')):
			_dir = host[:-1] + _dir.replace('\n', '')
		else:
			_dir = host + _dir.replace('\n', '')
			
		if(_dir not in directories):
			directories.append(_dir)
		else:
			continue
	
	extensions = []
	word_dirs = []
	fullURLs = []
	try:
		x = open('../../wordlists/extensions.txt')
		exts = x.readlines()
		for ext in exts:
			extensions.append(ext.replace('\n', ''))	
		x.close()
	except Exception:
		os.system('clear')
		print(banner)
		print(scanType)
		print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Failed to open extension list\n')
		pass

	bruteCount = 0
	downloaded = []
	for base in directories:
		try:
			x = open('../../wordlists/common.txt', 'r')
			words = x.readlines()
		except Exception:
			os.system('clear')
			print(banner)
			print(scanType)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Failed to open directory list\n')
			quit()

		try:
			for word in words:
				for ext in extensions:
					url = base + word.replace('\n', '') + ext.replace(' ', '')
					os.system('clear')
					print(banner)
					print(scanType)
					print(bc.BC + ' Trying to download: ' + bc.GC + url)
					try:
						req = requests.get(url, headers=headers)
						bruteCount += 1
						if(req.status_code == 200):
							try:
								try:
									wget.download(url)
									time.sleep(0.5)
									downloaded.append(word.replace('\n', '') + ext.replace(' ', ''))
								except Exception:
									continue
							except KeyboardInterrupt:
								continue
						else:
							continue
					except Exception:
						continue
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			print(scanType)
			print(sBan + ' [' + bc.GC + 'DOWNLOADED' + bc.BC + '] Brute Force results:')
			collected = 0
			for download in downloaded:
				collected += 1
				print(bc.GC + '\t' + download)
			
			if(collected == 0):
				print(bc.RC + '\tNone')
				fPlace = 'files'
			elif(collected == 1):
				fPlace = 'file'
			else:
				fPlace = 'files'

			print('\n' + sBan + ' Scan Complete for Host: ' + bc.GC + host)
			print(sBan + ' Brute Forced: ' + bc.GC + str(bruteCount) + ' directories')
			print(sBan + ' Downloaded Disallowed Entries: ' + bc.GC + str(collected) + ' ' + fPlace)
			print(sBan + ' Useful data may have been downloaded to ' + bc.GC + '/Pulled-Data/' + setKey + '/\n')

			os.system('rm -rf modules/__pycache__/ ../../modules/__pycache__/')
			quit()

	os.system('clear')
	print(banner)
	print(scanType)
	print(sBan + ' [' + bc.GC + 'DOWNLOADED' + bc.BC + '] Brute Force results:')
	collected = 0
	for download in downloaded:
		collected += 1
		if(collected == 0):
			print(bc.RC + '\tNone')
		else:
			print(bc.GC + '\t' + download)
	if(collected == 0):
		print(bc.RC + '\tNone')
		fPlace = 'files'
	elif(collected == 1):
		fPlace = 'file'
	else:
		fPlace = 'files'
			
	print('\n' + sBan + ' Scan Complete for Host: ' + bc.GC + host)
	print(sBan + ' Brute Forced: ' + bc.GC + str(bruteCount) + ' directories')
	print(sBan + ' Downloaded Disallowed Entries: ' + bc.GC + str(collected) + ' ' + fPlace)
	print(sBan + ' Useful data may have been downloaded to ' + bc.GC + '/Pulled-Data/' + setKey + '/\n')

	os.system('rm -rf modules/__pycache__/ ../../modules/__pycache__/')
	quit()
