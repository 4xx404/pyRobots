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
scanType = bc.BC + ' Scan Type: ' + bc.GC + 'Quick Scan\t\t' + bc.BC + 'Scan Speed: ' + bc.GC +'Fast\n'

os.system('clear')
print(banner)

def quick():
	print(scanType)
	print(infoBanner + " Enter " + bc.GC + "#//" + bc.BC + " to return to the main menu" + infoBanner)
	print(infoBanner + " Include " + bc.GC + "http://" + bc.BC + " | " + bc.GC + "https://" + bc.BC + " in the URL" + infoBanner + '\n')
	
	try:
		host = str(input(bc.BC + " URL: " + bc.GC))
		if host == '#//':
			os.system('clear')
			os.system(banner)
			from pyRobots import robotMenu
			robotMenu()

		if host[-1] == '/':
			ext = 'robots.txt'
		elif host[-1] != '/':
			ext = '/robots.txt'
		else:
			os.system('clear')
			print(banner)
			print(scanType)
			print(errorBanner + " Invalid URL" + errorBanner)
			quick()
		
		if 'http://' in host:
			url = host+ext
		elif 'https://' in host:
			url = host+ext
		else:
			os.system('clear')
			print(banner)
			print(scanType)
			print(errorBanner + " Invalid URL" + errorBanner + "\n")
			quick()

		print('\n' + infoBanner + " Trying Host: " + bc.GC + url + bc.BC + " for robots.txt file" + infoBanner)
		time.sleep(2)

		try:
			response = requests.get(url)
		except Exception:
			os.system('clear')
			print(banner)
			print(scanType)
			print(errorBanner + " Failed to Query Host: " + bc.GC + url + bc.BC + errorBanner + "\n")
			time.sleep(1)
			quick()
	
		if(response.status_code == 200):
			time.sleep(1)
			print(successBanner + " Host: " + bc.GC + url + bc.BC + " includes robots.txt file" + successBanner)
			
			try:
				os.mkdir('Pulled-Data')
				time.sleep(1)
			except FileExistsError:
				pass
			except Exception:
				os.system('clear')
				print(banner)
				print(errorBanner + " Failed to create " + bc.RC + "/Pulled-Data/" + bc.BC + " Directory" + errorBanner + "\n")
				time.sleep(1)
				quick()
			
			os.chdir('Pulled-Data')
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
				quick()
				
			os.chdir(setKey)
			time.sleep(1)
			print(bc.BC + " Starting Download for robots.txt...\n")
			time.sleep(1)

			try:
				os.system('wget ' + url)
				os.system('clear')
				print(banner)
				print(scanType)
				print(successBanner + " Successfully Downloaded: " + bc.GC + url + successBanner)
				time.sleep(1)
				print(infoBanner + " Loading robots.txt for Host: " + bc.GC + host + infoBanner)
				time.sleep(2)
			except Exception:
				os.system('clear')
				print(banner)
				print(scanType)
				print(errorBanner + " Failed to Download: " + bc.GC + url + errorBanner + "\n")
				time.sleep(1)
				quick()

			try:
				robotsTxt = open('robots.txt', 'r')
				lines = robotsTxt.readlines()
				print("\n" + successBanner + " robots.txt results for Host: " + bc.GC + host + bc.BC + successBanner + "\n")
	
			except Exception:
				os.system('clear')
				print(banner)
				print(scanType)
				print(errorBanner + " Failed to display robots.txt" + errorBanner + "\n")
				time.sleep(1)
				quick()

			for line in lines:
				if line.startswith('Disallow: '):
					if host.endswith('/'):
						os.system('clear')
						print(banner)
						print(scanType)
						ext = host + line.replace('\n', '').replace('Disallow: /', '')
						print(bc.BC + ' Trying to Download: ' + bc.GC + ext)
						time.sleep(1)
						os.system('wget ' + ext)

					else:
						os.system('clear')
						print(banner)
						print(scanType)
						ext = host + line.replace('\n', '').replace('Disallow: ', '')
						print(bc.BC + ' Trying to Download: ' + bc.GC + ext)
						time.sleep(1)
						os.system('wget ' + ext)

			os.system('clear')
			print(banner)
			print(scanType)
			for x in lines:
				if x.startswith('Disallow: '):
					print(bc.BC + " " + x.replace('\n', '').replace('Disallow: ', ''))
					
			os.system('rm -rf ../../__pycache__/')

			print("\n" + successBanner + " Scan Complete for Host: " + bc.GC + host + successBanner)
			print(successBanner + " Collected: " + bc.GC + "robots.txt" + successBanner)
			print(successBanner + " Collected: " + bc.GC + "disallowed entries" + successBanner + "\n")
			print(successBanner + " Useful data may have been downloaded to " + bc.GC + "/Pulled-Data/" + setKey + "/" + successBanner + '\n')
			quit()

		else:
			os.system('clear')
			print(banner)
			print(scanType)
			print(errorBanner + " Host: " + bc.GC + url + bc.BC + " does not include robots.txt file" + errorBanner)
			time.sleep(1)
			print(bc.BC + " Ignoring Download Attempt...")
			time.sleep(1)
			quick()

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
