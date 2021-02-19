#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
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

os.system('clear')
print(banner)

def robot():
	print(infoBanner + " Include " + bc.GC + "http://" + bc.BC + " | " + bc.GC + "https://" + bc.BC + " in the URL" + infoBanner)

	host = str(input(bc.BC + " URL: " + bc.GC))

	if host[-1] == '/':
		ext = 'robots.txt'
	elif host[-1] != '/':
		ext = '/robots.txt'
	else:
		os.system('clear')
		print(banner)
		print(errorBanner + " Invalid URL" + errorBanner)
		robot()
		
	if 'http://' in host:
		url = host+ext
	elif 'https://' in host:
		url = host+ext
	else:
		os.system('clear')
		print(banner)
		print(errorBanner + " Invalid URL" + errorBanner + "\n")
		robot()

	print('\n' + infoBanner + " Trying Host: " + bc.GC + url + bc.BC + " for robots.txt file" + infoBanner)
	time.sleep(2)

	try:
		response = requests.get(url)
	except Exception:
		os.system('clear')
		print(banner)
		print(errorBanner + " Failed to Query Host: " + bc.GC + url + bc.BC + errorBanner + "\n")
		time.sleep(1)
		robot()
	
	if(response.status_code == 200):
		time.sleep(1)
		print(successBanner + " Host: " + bc.GC + url + bc.BC + " includes robots.txt file" + successBanner)
		key = random.randrange(0, 99999999)
		try:
			setKey = str(key)
			os.mkdir(setKey)
			time.sleep(1)
		except FileExistsError:
			pass
		except Exception:
			os.system('clear')
			print(banner)
			print(errorBanner + " Failed to create " + setKey + " Directory" + errorBanner + "\n")
			time.sleep(1)
			robot()
		
		print(bc.BC + " Starting Download for robots.txt...\n")
		time.sleep(1)
		os.chdir(setKey)
		time.sleep(1)

		try:
			os.system('wget ' + url)
			time.sleep(1)
			print(successBanner + " Successfully Downloaded: " + bc.GC + url + successBanner)
			time.sleep(1)
			print(infoBanner + " Loading robots.txt for Host: " + bc.GC + host + infoBanner)
			time.sleep(2)
		except Exception:
			os.system('clear')
			print(banner)
			print(errorBanner + " Failed to Download: " + bc.GC + url + errorBanner + "\n")
			time.sleep(1)
			robot()

		try:
			robotsTxt = open('robots.txt', 'r')
			lines = robotsTxt.readlines()
			print("\n" + successBanner + " robots.txt results for Host: " + bc.GC + host + bc.BC + successBanner + "\n")

		except Exception:
			os.system('clear')
			print(banner)
			print(errorBanner + " Failed to display robots.txt" + errorBanner + "\n")
			time.sleep(1)
			robot()

		for line in lines:
			if line.startswith('Disallow: '):
				if host.endswith('/'):
					ext = host + line.replace('\n', '').replace('Disallow: /', '')
					os.system('wget ' + ext)
					time.sleep(1)
					os.system('clear')
					print(banner)
					print(bc.BC + ' Downloading: ' + bc.GC + ext)

				else:
					ext = host + line.replace('\n', '').replace('Disallow: ', '')
					os.system('wget ' + ext)
					time.sleep(1)
					os.system('clear')
					print(banner)
					print(bc.BC + ' Downloading: ' + bc.GC + ext)
		
		os.system('clear')
		print(banner)
		for x in lines:
			if x.startswith('Disallow: '):
				print(bc.BC + " " + x.replace('\n', '').replace('Disallow: ', ''))
		
		print("\n" + successBanner + " Host Scan Complete" + successBanner)
		print(successBanner + " Check /Pulled-Data/ for Other Files/Directories that may have been downloaded" + successBanner + '\n')
		print(successBanner + " Collected: " + bc.GC + "robots.txt" + successBanner)
		print(successBanner + " Collected: " + bc.GC + "disallowed entries" + successBanner + "\n")
		quit()
	else:
		os.system('clear')
		print(banner)
		print(errorBanner + " Host: " + bc.GC + url + bc.BC + " does not include robots.txt file" + errorBanner)
		time.sleep(1)
		print(bc.BC + " Ignoring Download Attempt...")
		time.sleep(1)
		robot()

if __name__ == '__main__':
	robot()
