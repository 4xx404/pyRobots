#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

sys.dont_write_bytecode = True

class Config:
	def __init__(self):
		self.ActiveUserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        
		self.Headers = {
			"Accept-Language": "en-US,en;q=0.5",
			"Cache-Control": "no-cache", 
			"User-Agent": self.ActiveUserAgent
		}
        
		self.ActiveCrawlDelay = 0