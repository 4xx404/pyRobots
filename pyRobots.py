#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, tldextract
from tld import get_tld

sys.dont_write_bytecode = True

from Core.Stylesheet.Styling import bc, sd
from Core.Console import Console
from Core.Commands import Command
from Core.Input import Input
from Core.Validity import Validation

from Core.Scanners.QuickScan import QuickScanner

class PyRobots:
	def __init__(self):
		self.Console = Console()
		self.Cmd = Command()
		self.Input = Input()
		self.Validator = Validation()		
		self.CreateOutputDirectory()

	def CreateOutputDirectory(self) -> None:
		try:
			os.mkdir("output")
		except FileExistsError:
			pass
		except Exception as e:
			self.Cmd.Clear(f"Could not create {bc.RC}/output/{bc.BC} directory\n {e}\n", True)

	def Start(self):		
		try:
			Host = self.Input.SetHostUrl()
			SetKey = tldextract.extract(Host).domain
			
			QuickScanner(Host, SetKey).Start()
		except KeyboardInterrupt:
			self.Cmd.Clear(f"\n{sd.eBan}{bc.BC} Keyboard Interrupt\n", True)

		except Exception as e:
			self.Cmd.Clear(f"{sd.eBan}{bc.BC} Unexpected Error: {bc.RC}{str(e)}{bc.BC}\n", True)

if (__name__ == "__main__"):
	def Initiate():
		try:
			PyRobots().Start()
		except KeyboardInterrupt:
			quit()

	Command().Clear()
	Initiate()