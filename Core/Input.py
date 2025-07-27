#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

from Core.Stylesheet.Styling import bc
from Core.Console import Console
from Core.Commands import Command
from Core.Validity import Validation

class Input:
    def __init__(self):
        self.Console = Console()
        self.Cmd = Command()
        self.Validator = Validation()

    def SetHostUrl(self) -> str:
        while True:
            Url = str(input(f"{bc.BC} Host Url: {bc.GC}")).strip()

            if (not self.Validator.NotEmpty(Url)):
                self.Console.Error(f"Host Url is required")
                
                continue

            if (not self.Validator.Url(Url)):
                self.Console.Error(f"Invalid Host Url. Must start with {bc.RC}http://{bc.BC} or {bc.RC}https://{bc.BC}, and include a valid hostname")

                continue

            if (not Url.endswith("/")):
                Url += "/"

            return Url
