#!/usr/bin/env python3
# put "shait" in /usr/local/bin and chmod +x it so you can simply "shait moo" from your terminal

import hashlib
import sys

def shait(string):
    """
    Return a SHA256 hash of the string input
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

print(shait(sys.argv[1]))
