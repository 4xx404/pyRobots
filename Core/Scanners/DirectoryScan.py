#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, requests, time
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

from Core.Stylesheet.Styling import bc, sd
from Core.Console import Console
from Core.Config import Config
from Core.Commands import Command
from Core.Validity import Validation

from Core.RobotsTxt import RobotsTxt

sys.dont_write_bytecode = True

class DirectoryScanner:
	def __init__(self, Host: str, SetKey: str, RobotsTxt: RobotsTxt, UserAgent: str = "*"):
		self.Console = Console()
		self.Config = Config()
		self.Cmd = Command()
		self.Validator = Validation()
		self.RobotsTxt = RobotsTxt
		self.UserAgent = UserAgent

		self.Host = self.__CanonicalizeHost(Host)
		self.SetKey = SetKey
		self.Rules = self.RobotsTxt.UserAgentRules.get(self.UserAgent, {})

		self.Directories = self.Rules.get("directories", [])
		self.CrawlDelay = self.Rules.get("crawl_delay", 0)

		self.__FormatDirectories()

		self.ExtensionsWordlistPath = "./wordlists/extensions.txt"
		self.Extensions = []
		self.__LoadExtensions()

		self.CommonWordlistPath = "./wordlists/common.txt"
		self.CommonDirectories = []
		self.__LoadCommonDirectories()

		self.BruteCount = 0
		self.Downloaded = []

		self.OutputDirectory = f"./output/{self.SetKey}"
		os.makedirs(self.OutputDirectory, exist_ok=True)

	def __CanonicalizeHost(self, Host: str) -> str:
		Parsed = urlparse(Host)

		if (not Parsed.scheme):
			Host = f"http://{Host}"
		
		if (not Host.endswith("/")):
			Host += "/"
		
		return Host

	def __FormatDirectories(self) -> None:
		if not self.Validator.NotEmpty(self.Directories):
			self.Cmd.Clear(f"{sd.eBan} No directories were found in robots.txt\n", True)

		Formatted = []

		for Directory in self.Directories:
			Directory = str(Directory).strip().lstrip("/")
			Url = urljoin(self.Host, f"{Directory}/")

			if (Url not in Formatted):
				Formatted.append(Url)

		self.Directories = Formatted

	def __LoadExtensions(self) -> None:
		try:
			with open(self.ExtensionsWordlistPath) as FileReader:
				self.Extensions = [Line.strip() for Line in FileReader if self.Validator.NotEmpty(Line)]
		except Exception as e:
			self.Cmd.Clear(f"{sd.eBan} Could not open extensions wordlist file: {self.ExtensionsWordlistPath}\n {bc.RC}{str(e)}\n", False)

	def __LoadCommonDirectories(self) -> None:
		try:
			with open(self.CommonWordlistPath, "r") as FileReader:
				self.CommonDirectories = [Line.strip() for Line in FileReader if self.Validator.NotEmpty(Line)]
		except Exception as e:
			self.Cmd.Clear(f"{sd.eBan} Could not open common directories wordlist file: {self.CommonWordlistPath}\n {bc.RC}{str(e)}\n", True)

	def __DownloadSingle(self, FullUrl: str, OutputPath: str) -> tuple[str, bool]:
		if (self.CrawlDelay > 0):
			self.Console.Raw(f"[{bc.RC}Throttle{bc.BC}] Waiting {bc.RC}{self.CrawlDelay}s{bc.BC} before starting download for {bc.GC}{FullUrl}", False)

			time.sleep(self.CrawlDelay)
			
		try:
			Req = requests.get(FullUrl, headers=self.Config.Headers, stream=True, timeout=3)

			self.BruteCount += 1

			if (Req.status_code == 200):
				self.Console.Raw(f"Trying to download {bc.GC}{FullUrl}...", False, False)

				with open(OutputPath, "wb") as FileWriter:
					for Chunk in Req.iter_content(chunk_size=8192):
						if (Chunk):
							FileWriter.write(Chunk)
				
				return OutputPath, True
			
			elif (Req.status_code in [429, 403]):
				RetryAfter = int(Req.headers.get("Retry-After", self.CrawlDelay or 3))
				self.Console.Raw(f"[{bc.RC}{Req.status_code} Throttled{bc.BC}] Backing off {bc.RC}{RetryAfter}s{bc.BC} for {bc.GC}{FullUrl}")
				
				time.sleep(RetryAfter)

				return OutputPath, False
			else:
				self.Console.Raw(f"[{bc.RC}{Req.status_code}{bc.BC}] Skipping {bc.GC}{FullUrl}")

		except Exception:
			self.Console.Raw(f"{bc.RC}Failed: {FullUrl}")

		return OutputPath, False
	
	def __GetMaxWorkers(self) -> int:
		if (self.CrawlDelay > 0):
			return 1 # Limit due to crawl-delay directive being set.


		return 20 # Default when crawl-delay directive is not set.

	def Start(self) -> None:
		self.Console.Raw(f"Creating directory data. This may take a moment.")

		MaxWorkers = self.__GetMaxWorkers()
		Futures = []
		
		with ThreadPoolExecutor(max_workers=MaxWorkers) as Executor:
			for BaseUrl in self.Directories:				
				for Common in self.CommonDirectories:				
					for Extension in self.Extensions:
						FullUrl = urljoin(BaseUrl, f"{Common}{Extension}")
						FileName = f"{Common}{Extension}"
						OutputPath = os.path.join(self.OutputDirectory, FileName)

						Futures.append(Executor.submit(self.__DownloadSingle, FullUrl, OutputPath))

			for Future in as_completed(Futures):
				FilePath, Success = Future.result()

				if (Success):
					self.Downloaded.append(os.path.basename(FilePath))

		self.DisplayResults()

	def DisplayResults(self) -> None:
		self.Cmd.Clear(f"{sd.sBan} [{bc.GC}DOWNLOADED{bc.BC}] Brute Force results:", False)

		if self.Validator.NotEmpty(self.Downloaded):
			for File in self.Downloaded:
				self.Console.Raw(f"{bc.GC}{File}", False, True)
		else:
			self.Console.Raw(f"{bc.RC}None", False, True)

		FilePlaceholder = "file" if len(self.Downloaded) == 1 else "files"

		self.Console.Raw(f"\n{sd.sBan} Scan complete for host:{bc.GC} {self.Host}", False)
		self.Console.Raw(f"{sd.sBan} Brute Forced:{bc.GC} {self.BruteCount} directories", False)
		self.Console.Raw(f"{sd.sBan} Downloaded disallowed entries:{bc.GC} {len(self.Downloaded)} {FilePlaceholder}", False)
		self.Console.Raw(f"{sd.sBan} Useful data may have been downloaded to {bc.GC}/output/{self.SetKey}/", True)

		quit()
