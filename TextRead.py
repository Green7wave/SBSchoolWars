import os
import sys
import shutil
import numpy as np 

# V 0.1

class readtext():
    def __init__(self, rootp):
        self.rootp = rootp
        if not rootp.endswith("\\"):
            self.rootp = rootp + "\\"


    def giverantxt(self, textfilepath):
        with open(self.rootp +  textfilepath, encoding='utf-8') as f:
            content = f.readlines()
            ri = np.random.randint(len(content))
            return content[ri]
        
    def givefulltext(self, textfilepath):
        with open(self.rootp +  textfilepath, encoding='utf-8') as f:
            content = f.read()
            return content
        
    def givetextline(self, textfilepath, lines = 1):
        with open(self.rootp +  textfilepath, encoding='utf-8') as f:
            readline = 1
            while readline != lines:
                readline += 1
                f.readline()
            return f.readline()
            
