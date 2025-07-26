#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from Core.Stylesheet.Styling import bc, sd
from Core.Console import Console
from Core.Commands import Command
from Core.Validity import Validation

sys.dont_write_bytecode = True

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
