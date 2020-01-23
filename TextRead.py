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
        with open(self.rootp + "\\" + textfilepath) as f:
            content = f.readlines()
            ri = np.random.randint(len(content))
            return content[ri]
        
    def givefulltext(self, textfilepath):
        with open(self.rootp + "\\" + textfilepath) as f:
            content = f.read()
            return content
            
