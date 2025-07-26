#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from urllib.parse import urlparse

sys.dont_write_bytecode = True

class Validation:
    def __init__(self):
        pass

    def NotEmpty(self, Object: str or list or dict = None) -> bool: # type: ignore
        if(Object != None):
            if(type(Object) == str and Object.strip() != ""):
                return True
            elif(type(Object) == list and len(Object) > 0):
                return True
            elif(type(Object) == dict and len(Object.keys()) > 0):
                return True
            
        return False
    
    def Url(self, Url: str) -> bool:
        if (not isinstance(Url, str) or not Url.strip()):
            return False

        Parsed = urlparse(Url.strip())

        return Parsed.scheme in ("http", "https") and bool(Parsed.netloc)