#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

from Core.Stylesheet.Styling import sd, bc
from Core.Validity import Validation

class Console:
    def __init__(self):
        self.Validator = Validation()

    def Success(self, Message: str, AppendNewLine: bool = True) -> None:
        if (self.Validator.NotEmpty(Message)):
            SuccessString = f" {sd.sBan} {Message.strip()}{bc.BC}"

            if (AppendNewLine):
                SuccessString += "\n"

            print(SuccessString)

    def Info(self, Message: str, AppendNewLine: bool = True) -> None:
        if (self.Validator.NotEmpty(Message)):
            InfoString = f" {sd.iBan} {Message.strip()}{bc.BC}"

            if (AppendNewLine):
                InfoString += "\n"

            print(InfoString)

    def Error(self, Message: str, AppendNewLine: bool = True) -> None:
        if (self.Validator.NotEmpty(Message)):
            ErrorString = f" {sd.eBan} {Message.strip()}{bc.BC}"

            if (AppendNewLine):
                ErrorString += "\n"

            print(ErrorString)

    def Raw(self, Message: str, AppendNewLine: bool = True, IndentMessage = False) -> None:
        if (self.Validator.NotEmpty(Message)):
            RawString = f" {bc.BC}{Message.strip()}{bc.BC}"

            if (AppendNewLine):
                RawString += "\n"

            if (IndentMessage):
                RawString = f"\t {RawString}"

            print(RawString)