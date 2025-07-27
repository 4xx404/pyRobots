#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, platform, os
sys.dont_write_bytecode = True

from Core.Stylesheet.Styling import Banner
from Core.Console import Console
from Core.Validity import Validation

class Command:
    def __init__(self):
        self.Console = Console()
        self.Validator = Validation()

        self.CommandMatrix = {
            "windows": {
                "clear": "cls"
            },

            "linux": {
                "clear": "clear"
            },
            
            "darwin": {
                "clear": "clear"
            }
        }

    def GetOS(self) -> str:
        return platform.system().lower()

    def Clear(self, Message: str = None, ShouldQuit: bool = False) -> None:
        Platform = self.GetOS()

        os.system(self.CommandMatrix[Platform]["clear"])
    
        self.Console.Raw(Banner.Logo)
    
        if (self.Validator.NotEmpty(Message)):
            self.Console.Raw(Message)
    
        if (ShouldQuit):
            quit()