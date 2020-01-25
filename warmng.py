# WAR manager

class country():
    def __init__(self, name, warmen, bmp, statenum, dmid):
        self.name = name
        self.warmen = warmen
        self.bmp = bmp
        self.dmid = dmid
        self.statenum = statenum
        
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
            
    def addlosses(self, atklosses, deflosses):
        self.atklossinfo.append(atklosses)
        self.deflossinfo.append(deflosses)
            
        
        