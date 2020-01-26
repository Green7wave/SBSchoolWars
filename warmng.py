# WAR manager

from random import randint

class country():
    def __init__(self, name, warmen, bmp, statenum, dmid):
        self.name = name
        self.warmen = int(warmen)
        self.bmp = int(bmp)
        if dmid.lower() == "bot":
            self.dmid = dmid.lower()
        else:
            self.dmid = int(dmid)
        self.statenum = int(statenum)
        
    def modifybmp(self, percentage):
      modify = self.bmp * percentage * 0.01
      self.bmp = self.bmp + modify
      return self.bmp
    
class warstarter():
    def __init__(self, attacker, defender, atkdir = [], atkmil = [], atkmen = [], defdir = [], defmil = [], defmen = []):
        # asgining
        self.attacker = attacker
        self.defender = defender
        self.atkmil = atkmil
        self.defmil = defmil
        self.atkmen = atkmen
        self.defmen = defmen
        self.atkdir = atkdir
        self.defdir = defdir
        
        # SPECIAL VARIABLES
        self.atkloss = 0
        self.defloss = 0
        self.atklossinfo = []
        self.deflossinfo = []
        self.atkclos = 0
        self.defclos = 0
        
        self.states = defender.statenum
        self.leftstates = defender.statenum
        self.gotstates = 0
        
        self.atkdice = None
        self.defdice = None
        # counting miliatry power
        # attacker
        self.atkpow = attacker.bmp
        for i in atkdir:
            add = i.bmp * 0.8
            self.atkpow += add
        for i in atkmil:
            add = i.bmp * 0.2
            self.atkpow += add
        for i in atkmen:
            add = i.bmp * 0.4
            self.atkpow += add
        self.atkpow = round(self.atkpow)
        
        # defender
        self.defpow = defender.bmp
        for i in defdir:
            add = i.bmp * 0.8
            self.defpow += add
        for i in defmil:
            add = i.bmp * 0.2
            self.defpow += add
        for i in defmen:
            add = i.bmp * 0.4
            self.defpow += add
        self.defpow = round(self.defpow)
        
        self.atklife = self.atkpow
        self.deflife = self.defpow    
        
        
    def addlosses(self):
        self.atklossinfo.append(self.atkloss)
        self.deflossinfo.append(self.defloss)
        self.atkloss = 0
        self.defloss = 0
    
    def rolldice(self):
        return randint(1, 6)
        
    def decide(self):
        #determine loss
        if self.atkdice == self.defdice:
            if self.atklife == 1 or self.deflife == 1:
                pass
            else:
                self.atklife -= 1
                self.deflife -= 1
                self.atkloss += 1
                self.defloss += 1
        elif self.atkdice > self.defdice:
            self.deflife -= 1
            self.defloss += 1
        elif self.atkdice < self.defdice:
            self.atklife -= 1
            self.atkloss += 1
            
        #see if its the end
        if self.atklife == 0 and self.gotstates != 0:
            self.gotstates -= 1
            self.leftstates += 1
            self.atkclos += 1
            self.atklife = self.atkpow
            self.deflife = self.defpow
            return 3
        
        elif self.deflife == 0 and self.leftstates != 1:
            self.gotstates += 1
            self.leftstates -= 1
            self.atkclos += 1
            self.atklife = self.atkpow
            self.deflife = self.defpow
            return 4
            
        elif self.atklife == 0:
            self.gotstates -= 1
            self.leftstates += 1
            self.atkclos += 1
            self.atklife = self.atkpow
            self.deflife = self.defpow
            return 1
        
        elif self.deflife == 0:
            self.gotstates += 1
            self.leftstates -= 1
            self.atkclos += 1
            self.atklife = self.atkpow
            self.deflife = self.defpow
            return 2
        
        
        else:
            c = randint(1, 10)
            if c > 5:
                return 7
            else:
                return 0