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
scanType = bc.BC + ' Scan Type: ' + bc.GC + 'Advanced Scan\t\t' + bc.BC + 'Scan Speed: ' + bc.RC +'Very Slow\n'

os.system('clear')
print(banner)

def advanced():
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
			advanced()
		
		if 'http://' in host:
			url = host+ext
		elif 'https://' in host:
			url = host+ext
		else:
			os.system('clear')
			print(banner)
			print(scanType)
			print(errorBanner + " Invalid URL" + errorBanner + "\n")
			advanced()

		print(infoBanner + " Trying Host: " + bc.GC + url + bc.BC + " for robots.txt file" + infoBanner + '\n')
		time.sleep(2)

		try:
			response = requests.get(url)
		except Exception:
			os.system('clear')
			print(banner)
			print(scanType)
			print(errorBanner + " Failed to Query Host: " + bc.GC + url + bc.BC + errorBanner + "\n")
			time.sleep(1)
			advanced()
	
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
				advanced()
			
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
				advanced()
				
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
				advanced()

			try:
				setRobotsTxt = 'robots.txt'
				robotsTxt = open(setRobotsTxt, 'r')
				lines = robotsTxt.readlines()
			except Exception:
				os.system('clear')
				print(banner)
				print(scanType)
				print(errorBanner + " Failed to display robots.txt" + errorBanner + "\n")
				time.sleep(1)
				advanced()

			print('\n' + infoBanner + " Leave " + bc.GC + "EMPTY" + bc.BC + " for Default Wordlist: " + bc.GC + "common.txt" + infoBanner)
			uWordlist = str(input(bc.BC + ' Wordlist: ' + bc.GC))
			if uWordlist == '':
				setWordlist = '../../wordlists/common.txt'
				print(infoBanner + " Wordlist defaulting to " + bc.GC + setWordlist + infoBanner)
				time.sleep(1)
			else:
				setWordlist = uWordlist
				print(infoBanner + " Loading Wordlist: " + bc.GC + setWordlist + infoBanner)
				time.sleep(1)
			try:
				wordlist = open(setWordlist, 'r')
				words = wordlist.readlines()
			except Exception:
				os.system('clear')
				print(banner)
				print(scanType)
				print(errorBanner + " Failed to open " + bc.RC + wordlist + errorBanner + "\n")
				time.sleep(1)
				advanced()

			print('\n' + infoBanner + " Leave " + bc.GC + "EMPTY" + bc.BC + " for Default Extension List: " + bc.GC + "extensions.txt" + infoBanner)
			uExtlist = str(input(bc.BC + ' Extension List: ' + bc.GC))
			if uExtlist == '':
				setExtlist = '../../wordlists/extensions.txt'
				print(infoBanner + " Extension List defaulting to " + bc.GC + setExtlist + infoBanner)
				time.sleep(1)
			else:
				setExtlist = uExtlist
				print(infoBanner + " Loading Extension List: " + bc.GC + setWordlist + infoBanner)
				time.sleep(1)
			try:
				extlist = open(setExtlist, 'r')
				extensions = extlist.readlines()
			except Exception:
				os.system('clear')
				print(banner)
				print(scanType)
				print(errorBanner + " Failed to open " + bc.RC + setExtlist + errorBanner + "\n")
				time.sleep(1)
				advanced()
			
			if host.endswith('/'):
				newHost = host
			else:
				newHost = host + "/"

			print('\n' + infoBanner + " Leave " + bc.GC+ "EMPTY" + bc.BC + " or enter " + bc.GC + "0" + bc.BC + " for Default Delay" + infoBanner)
			rDelay = str(input(bc.BC + ' Request Delay(Seconds): ' + bc.GC))
			if rDelay == '' or rDelay == '0' or rDelay == '1':
				setRDelay = 1
			else:
				setRDelay = int(rDelay)

			for line in lines:
				if line.startswith('Disallow: /'):
					line = line.replace('\n', '').replace('Disallow: /', '')
					if line.endswith('/'):
						for word in words:
							word = word.replace('\n', '')
							newURLS = []
							if word.startswith('.'):
								removeSpecialCharWord = word[1:]
								for x in extensions:
									newURL = newHost + line + word + x
									newURLS.append(newURL)
									newNoSpecialCharURL = newHost + line + removeSpecialCharWord + x
									newURLS.append(newNoSpecialCharURL)
		
								for a in newURLS:
									os.system('clear')
									print(banner)
									print(scanType)
									print(bc.BC + ' Trying to Download: ' + bc.GC + a)
									time.sleep(setRDelay)
									os.system('wget ' + a)
									
							elif word.startswith('_'):
								removeSpecialCharWord = word[1:]
								for x in extensions:
									newURL = newHost + line + word + x
									newURLS.append(newURL)
									newNoSpecialCharURL = newHost + line + removeSpecialCharWord + x
									newURLS.append(newNoSpecialCharURL)
		
								for a in newURLS:
									os.system('clear')
									print(banner)
									print(scanType)
									print(bc.BC + ' Trying to Download: ' + bc.GC + a)
									time.sleep(setRDelay)
									os.system('wget ' + a)
							
							elif word.startswith('-'):
								removeSpecialCharWord = word[1:]
								for x in extensions:
									newURL = newHost + line + word + x
									newURLS.append(newURL)
									newNoSpecialCharURL = newHost + line + removeSpecialCharWord + x
									newURLS.append(newNoSpecialCharURL)
		
								for a in newURLS:
									os.system('clear')
									print(banner)
									print(scanType)
									print(bc.BC + ' Trying to Download: ' + bc.GC + a)
									time.sleep(setRDelay)
									os.system('wget ' + a)

							elif word.startswith('~'):
								removeSpecialCharWord = word[1:]
								for x in extensions:
									newURL = newHost + line + word + x
									newURLS.append(newURL)
									newNoSpecialCharURL = newHost + line + removeSpecialCharWord + x
									newURLS.append(newNoSpecialCharURL)
		
								for a in newURLS:
									os.system('clear')
									print(banner)
									print(scanType)
									print(bc.BC + ' Trying to Download: ' + bc.GC + a)
									time.sleep(setRDelay)
									os.system('wget ' + a)
							
							elif word.startswith('#'):
								removeSpecialCharWord = word[1:]
								for x in extensions:
									newURL = newHost + line + word + x
									newURLS.append(newURL)
									newNoSpecialCharURL = newHost + line + removeSpecialCharWord + x
									newURLS.append(newNoSpecialCharURL)
		
								for a in newURLS:
									os.system('clear')
									print(banner)
									print(scanType)
									print(bc.BC + ' Trying to Download: ' + bc.GC + a)
									time.sleep(setRDelay)
									os.system('wget ' + a)
							
							elif word.startswith('@'):
								removeSpecialCharWord = word[1:]
								for x in extensions:
									newURL = newHost + line + word + x
									newURLS.append(newURL)
									newNoSpecialCharURL = newHost + line + removeSpecialCharWord + x
									newURLS.append(newNoSpecialCharURL)
		
								for a in newURLS:
									os.system('clear')
									print(banner)
									print(scanType)
									print(bc.BC + ' Trying to Download: ' + bc.GC + a)
									time.sleep(setRDelay)
									os.system('wget ' + a)
									
							elif word.startswith('_@'):
								removeSpecialCharWord = word[1:]
								for x in extensions:
									newURL = newHost + line + word + x
									newURLS.append(newURL)
									newNoSpecialCharURL = newHost + line + removeSpecialCharWord + x
									newURLS.append(newNoSpecialCharURL)
		
								for a in newURLS:
									os.system('clear')
									print(banner)
									print(scanType)
									print(bc.BC + ' Trying to Download: ' + bc.GC + a)
									time.sleep(setRDelay)
									os.system('wget ' + a)

							elif word.startswith('@_'):
								removeSpecialCharWord = word[1:]
								for x in extensions:
									newURL = newHost + line + word + x
									newURLS.append(newURL)
									newNoSpecialCharURL = newHost + line + removeSpecialCharWord + x
									newURLS.append(newNoSpecialCharURL)
		
								for a in newURLS:
									os.system('clear')
									print(banner)
									print(scanType)
									print(bc.BC + ' Trying to Download: ' + bc.GC + a)
									time.sleep(setRDelay)
									os.system('wget ' + a)
							else:
								for x in extensions:
									newURL = newHost + line + word + x
									newURLS.append(newURL)

							for a in newURLS:
								os.system('clear')
								print(banner)
								print(scanType)
								print(bc.BC + ' Trying to Download: ' + bc.GC + a)
								time.sleep(setRDelay)
								os.system('wget ' + a)

					if line != line.endswith('/'):
						newURL = newHost + line
						os.system('clear')
						print(banner)
						print(scanType)
						print(bc.BC + ' Trying to Download: ' + bc.GC + newURL)
						time.sleep(setRDelay)
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
			advanced()

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
