#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, requests, time
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.dont_write_bytecode = True

from Core.Stylesheet.Styling import bc, sd
from Core.Console import Console
from Core.Config import Config
from Core.Commands import Command
from Core.Validity import Validation

from Core.RobotsTxt import RobotsTxt
from Core.Scanners.DirectoryScan import DirectoryScanner

class QuickScanner:
	def __init__(self, Host: str, SetKey: str):
		self.Console = Console()
		self.Config = Config()
		self.Cmd = Command()
		self.Validator = Validation()

		self.Host = Host if Host.endswith("/") else Host + "/"
		self.SetKey = SetKey
		self.OutputDirectory = f"./output/{self.SetKey}"

		self.RobotsTxt = RobotsTxt(self.Host, self.OutputDirectory)
		self.DownloadedFiles = []

	def CreateSetKeyDirectory(self):
		try:
			os.makedirs(self.OutputDirectory, exist_ok=True)
		except Exception as e:
			self.Cmd.Clear(f"{sd.eBan} Failed to create directory: {self.OutputDirectory}\n {bc.RC}{str(e)}\n", True)

	def DownloadSingleFile(self, Path: str) -> None:
		Url = urljoin(self.Host, Path)

		# Preserve folder structure to avoid overwrites
		LocalPath = os.path.join(self.OutputDirectory, Path.lstrip("/"))
		os.makedirs(os.path.dirname(LocalPath), exist_ok=True)

		Delay = self.RobotsTxt.CrawlDelay or 0

		if (Delay > 0):
			self.Console.Raw(f"[{bc.RC}Throttle{bc.BC}] Waiting {bc.RC}{Delay}s{bc.BC} before fetching {bc.GC}{Url}", False)

			time.sleep(Delay)

		try:
			Response = requests.get(Url, headers=self.Config.Headers, stream=True, timeout=5)

			if (Response.status_code in [429, 403]):
				RetryAfter = int(Response.headers.get("Retry-After", Delay or 3))
				self.Console.Raw(f"{bc.RC}[{Response.status_code}] Throttled. Backing off {RetryAfter}s for {Url}")

				time.sleep(RetryAfter)

				return

			if (Response.status_code == 200):
				with open(LocalPath, "wb") as FileWriter:
					for Chunk in Response.iter_content(chunk_size=8192):
						if Chunk:
							FileWriter.write(Chunk)

				self.DownloadedFiles.append(Url)
				self.Console.Success(f"Downloaded: {bc.GC}{Url}", False)

		except Exception as e:
			self.Console.Raw(f"{bc.RC}Failed: {Url}\n {bc.RC}{str(e)}\n")


	def DownloadFiles(self) -> None:
		DisallowedPaths = self.RobotsTxt.Disallowed
		AllowedPaths = self.RobotsTxt.Allowed
		AllPaths = list(set(DisallowedPaths + AllowedPaths))

		Delay = self.RobotsTxt.CrawlDelay or 0
		MaxWorkers = 1 if Delay > 1 else 20

		if Delay > 0:
			for Path in AllPaths:
				self.DownloadSingleFile(Path)
		else:
			with ThreadPoolExecutor(max_workers=MaxWorkers) as executor:
				Futures = [executor.submit(self.DownloadSingleFile, Path) for Path in AllPaths]

				for _ in as_completed(Futures):
					pass

	def DownloadSitemaps(self):
		for SitemapUrl in self.RobotsTxt.Sitemap:
			try:
				Response = requests.get(SitemapUrl, headers=self.Config.Headers, timeout=5)

				if (Response.status_code == 200):
					FileName = os.path.basename(SitemapUrl)
					
					with open(os.path.join(self.OutputDirectory, FileName), "wb") as FileWriter:
						FileWriter.write(Response.content)

					self.Console.Success(f"Sitemap downloaded: {SitemapUrl}")
			except Exception as e:
				self.Console.Error(f"Failed to download sitemap: {SitemapUrl}\n {bc.RC}{str(e)}\n", True)

	def DisplayResults(self, ShowDirectoryScanPrompt: bool = True) -> None:
		print()
		self.Console.Raw(f"Scan complete for host: {bc.GC}{self.Host}", True)

		Plural = "files" if len(self.DownloadedFiles) != 1 else "file"
		self.Console.Raw(f"Downloaded disallowed entries: {bc.GC}{len(self.DownloadedFiles)} {Plural}", True)

		for Counter, Url in enumerate(self.DownloadedFiles, 1):
			self.Console.Raw(f"{bc.GC}output/{self.SetKey}/{str(Url).replace(self.Host, '')}", False, True)
            
			if (Counter == len(self.DownloadedFiles)):
				print()

		self.Console.Raw(f"Output in {bc.GC}{self.OutputDirectory}/")

		if (ShowDirectoryScanPrompt):
			self.PromptForDirectoryScan()

	def PromptForDirectoryScan(self):
		try:
			Prompt = input(f"{bc.BC} Brute Force Directories[{bc.GC}y{bc.BC}/{bc.GC}n{bc.BC}]: {bc.GC}").lower()
            
			if (Prompt == "y"):
				DirectoryScanner(self.Host, self.SetKey, self.RobotsTxt).Start()
		except KeyboardInterrupt:
			quit()

	def Start(self) -> None:
		try:
			if (requests.get(self.RobotsTxt.Url, headers=self.Config.Headers, timeout=5).status_code != 200):
				self.Cmd.Clear(f"{sd.eBan} robots.txt not found for {bc.GC}{self.Host}{bc.BC}\n", True)

			self.CreateSetKeyDirectory()
			self.RobotsTxt.Download(self.OutputDirectory)
			self.RobotsTxt.Parse()

			self.DownloadSitemaps()

			if (self.Validator.NotEmpty(self.RobotsTxt.Disallowed)):
				self.DownloadFiles()
				self.DisplayResults(True)
			else:
				self.Console.Error(f"No disallowed entries found for crawling.", True)

		except KeyboardInterrupt:
			self.DisplayResults(False)
			
			quit()
