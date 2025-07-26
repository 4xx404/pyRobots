#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, requests
from typing import List, Dict, Optional

from Core.Stylesheet.Styling import bc, sd
from Core.Console import Console
from Core.Config import Config
from Core.Commands import Command
from Core.Validity import Validation

sys.dont_write_bytecode = True

class RobotsTxt:
    def __init__(self, Host: str, OutputDirectory: str):
        self.Host = Host if Host.endswith("/") else f"{Host}/"
        self.LocalPath = os.path.join(OutputDirectory, "robots.txt")
        self.Url = f"{self.Host}robots.txt"

        self.Config = Config()
        self.Console = Console()
        self.Cmd = Command()
        self.Validator = Validation()

        self.Sitemap: List[str] = []
        self.UserAgentRules: Dict[str, Dict[str, Optional[List[str]]]] = {}
        self.CurrentUserAgent: str = "*"
        
        if ("*" not in self.UserAgentRules):
            self.UserAgentRules["*"] = {
                "disallow": [],
                "allow": [],
                "directories": [],
                "crawl_delay": 0
            }

    def Download(self, OutputDirectory: str) -> None:
        print()
        self.Console.Raw("Starting download for robots.txt...")

        try:
            Response = requests.get(self.Url, headers=self.Config.Headers, timeout=3)

            if Response.status_code != 200:
                self.Cmd.Clear(f"{sd.eBan} Could not download {bc.RC}robots.txt{bc.BC} from {bc.RC}{self.Host}{bc.BC}", True)

            os.makedirs(OutputDirectory, exist_ok=True)

            with open(self.LocalPath, "wb") as FileWriter:
                FileWriter.write(Response.content)

        except Exception as e:
            self.Cmd.Clear(f"{sd.eBan} Error downloading robots.txt: {bc.RC}{str(e)}", True)

    def Parse(self) -> List[str]:
        try:
            with open(self.LocalPath, "r", encoding="utf-8") as FileReader:
                Lines = [Line.strip() for Line in FileReader if (Line.strip() and not Line.startswith("#"))]
            
            CurrentAgents = ["*"]

            for Line in Lines:
                if (Line.lower().startswith("user-agent:")):
                    agent = Line.split(":", 1)[1].strip()

                    if (agent):
                        CurrentAgents.append(agent)
                        
                        if (agent not in self.UserAgentRules):
                            self.UserAgentRules[agent] = {
                                "disallow": [],
                                "allow": [],
                                "directories": [],
                                "crawl_delay": 0
                            }

                elif Line.lower().startswith("disallow:"):
                    path = Line.split(":", 1)[1].strip()

                    if (self.Validator.NotEmpty(path)):
                        for agent in CurrentAgents:
                            if (agent not in self.UserAgentRules):
                                self.UserAgentRules[agent] = {
                                    "disallow": [],
                                    "allow": [],
                                    "directories": [],
                                    "crawl_delay": 0
                                }

                            if (path.endswith("/")):
                                if (path not in self.UserAgentRules[agent]["directories"]):
                                    self.UserAgentRules[agent]["directories"].append(path)
                            else:
                                if (path not in self.UserAgentRules[agent]["disallow"]):
                                    self.UserAgentRules[agent]["disallow"].append(path)

                elif Line.lower().startswith("allow:"):
                    path = Line.split(":", 1)[1].strip()

                    if (self.Validator.NotEmpty(path)):
                        for agent in CurrentAgents:
                            if (agent not in self.UserAgentRules):
                                self.UserAgentRules[agent] = {
                                    "disallow": [],
                                    "allow": [],
                                    "directories": [],
                                    "crawl_delay": 0
                                }

                            if (path.endswith("/")):
                                if (path not in self.UserAgentRules[agent]["directories"]):
                                    self.UserAgentRules[agent]["directories"].append(path)
                            else:
                                if (path not in self.UserAgentRules[agent]["allow"]):
                                    self.UserAgentRules[agent]["allow"].append(path)

                elif Line.lower().startswith("crawl-delay:"):
                    value = Line.split(":", 1)[1].strip()
                    
                    try:
                        delay = float(value)

                        for agent in CurrentAgents:
                            self.UserAgentRules[agent]["crawl_delay"] = delay
                    except ValueError:
                        continue

                elif Line.lower().startswith("sitemap:"):
                    Sitemap = Line.split(":", 1)[1].strip()

                    if (self.Validator.NotEmpty(Sitemap)):
                        self.Sitemap.append(Sitemap)

        except Exception as e:
            self.Cmd.Clear(f"{sd.eBan} Could not parse robots.txt\n{bc.RC}{str(e)}", True)

        # print(self.UserAgentRules)
        # quit()

        return self.UserAgentRules.get("*", {}).get("disallow", [])

    # Compatibility properties for external access
    @property
    def Disallowed(self) -> List[str]:
        return self.UserAgentRules.get("*", {}).get("disallow", [])

    @property
    def Allowed(self) -> List[str]:
        return self.UserAgentRules.get("*", {}).get("allow", [])

    @property
    def Directories(self) -> List[str]:
        return self.UserAgentRules.get("*", {}).get("directories", [])

    @property
    def CrawlDelay(self) -> Optional[float]:
        return self.UserAgentRules.get("*", {}).get("crawl_delay", 0)
