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
scanType = bc.BC + ' Scan Type: ' + bc.GC + 'Extended Scan\t\t' + bc.BC + 'Scan Speed: ' + bc.BC +'Slow\n'

os.system('clear')
print(banner)

def extensive():
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
			extensive()
		
		if 'http://' in host:
			url = host+ext
		elif 'https://' in host:
			url = host+ext
		else:
			os.system('clear')
			print(banner)
			print(scanType)
			print(errorBanner + " Invalid URL" + errorBanner + "\n")
			extensive()

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
			extensive()
	
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
				extensive()
			
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
				extensive()
				
			os.chdir(setKey)
			time.sleep(1)
			print(bc.BC + " Starting Download for robots.txt...\n")
			time.sleep(1)

			try:
				os.system('wget -t 3 ' + url)
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
				extensive()

			try:
				robotsTxt = open('robots.txt', 'r')
				lines = robotsTxt.readlines()
			except Exception:
				os.system('clear')
				print(banner)
				print(scanType)
				print(errorBanner + " Failed to display robots.txt" + errorBanner + "\n")
				time.sleep(1)
				extensive()

			try:
				wordlist = open('../../wordlists/small.txt', 'r')
				words = wordlist.readlines()
			except Exception:
				os.system('clear')
				print(banner)
				print(scanType)
				print(errorBanner + " Failed to open " + bc.RC + wordlist + errorBanner + "\n")
				time.sleep(1)
				extensive()
			
			if host.endswith('/'):
				newHost = host
			else:
				newHost = host + "/"

			for line in lines:
				if line.startswith('Disallow: /'):
					line = line.replace('\n', '').replace('Disallow: /', '')
				
					if line.endswith('/'):
						for word in words:
							word = word.replace('\n', '')
							extensions = ['.asp', '.aspx', '.css', '.html', '.htm', '.xhtml', '.jhtml', '.jsp', '.jspx', '.js', '.pl', '.php', '.php3', '.php4', '.phtml', '.py', '.rb', '.rhtml', '.shtml', '.xml', '.rss', '.cgi', '.dll', '.png', '.jpg', '.jpeg', '.mp4', '.ogg', '.webm', '.txt', '.pdf', '.log', '.docx']
							for x in extensions:
								newURL = newHost + line + word + x
								os.system('clear')
								print(banner)
								print(scanType)
								print(bc.BC + ' Trying to Download: ' + bc.GC + newURL)
								time.sleep(1)
								os.system('wget ' + newURL)

					if line != line.endswith('/'):
						newURL = newHost + line
						os.system('clear')
						print(banner)
						print(scanType)
						print(bc.BC + ' Trying to Download: ' + bc.GC + newURL)
						time.sleep(1)
						os.system('wget ' + newURL)

			os.system('clear')
			print(banner)
			print(scanType)
			print(successBanner + " robots.txt results for Host: " + bc.GC + host + bc.BC + successBanner + "\n")
			for x in lines:
				if x.startswith('Disallow: '):
					print(bc.BC + " " + x.replace('\n', '').replace('Disallow: ', ''))

			print("\n" + successBanner + " Scan Complete for Host: " + bc.GC + host + successBanner)
			print(successBanner + " Collected: " + bc.GC + "robots.txt" + successBanner)
			print(successBanner + " Collected: " + bc.GC + "disallowed entries" + successBanner + "\n")
			print(successBanner + " Useful data may have been downloaded to " + bc.GC + "/Pulled-Data/" + setKey + "/" + successBanner + '\n')
			os.system('rm -rf ../../__pycache__/')
			quit()

		else:
			os.system('clear')
			print(banner)
			print(scanType)
			print(errorBanner + " Host: " + bc.GC + url + bc.BC + " does not include robots.txt file" + errorBanner)
			time.sleep(1)
			print(bc.BC + " Ignoring Download Attempt...")
			time.sleep(1)
			extensive()

	except KeyboardInterrupt:
		os.system('clear')
		print(banner)
		print(scanType)
		print(bc.BC + ' Clearing Cache...')
		os.system('rm -rf ../../__pycache__/')
		time.sleep(1)
		print(bc.BC + ' Closing pyRobots...')
		time.sleep(1)
		quit()
