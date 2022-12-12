'''
#######################################################################
Information needed (per game)
- Player name
- Player handle (1-S2-1-3591394)
- Player role (M/Z)
- Player Victory/Loss (1/0)

For Marines...
- Weapon used (+mods?)
- Kills
- Score
- Captures
- Marine Saves
- Alpha kills
- Z Structure kills
- Structures built (turrets, heal droids, psis)
- Experimental purchased (should include N/A)
- Total gas income (total & mined)
- Total gas spent

For Zombie...
- Marine Captures
- Important Rooms Captured
- Hangars Killed
- # of rooms captured
- Total Gas income (if info is available)
- Total Gas spent
- Alphas built
- Strains purchased
- Upgrades purchased
- # of Pod upgrades
- Structures built

#######################################################################
Information needed (per player) - just look at their latest bank files
#######################################################################
'''


class playerinfo():
    def __init__(self, name, pid, handle, role):
        self.playername = name
        self.pid = pid
        self.handle = handle
        self.playerrole = role
        self.victory = 0


class marineinfo(playerinfo):
    def __init__(self, name, pid, handle, role):
        super().__init__(name, pid, handle, role)
        self.weapon = ''
        self.kills = 0
        self.score = 0
        self.captures = 0
        self.saves = 0
        self.alphakills = 0
        self.zstructurekills = 0
        self.mstructurebuilt = 0
        self.experimentalpurchased = 0
        self.totalgasincome = 0
        self.totalgasspent = 0


class zombieinfo(playerinfo):
    def __init__(self, name, pid, handle, role):
        super().__init__(name, pid, handle, role)
        self.marinecaptures = 0
        self.roomcaptures = 0
        self.majorroomcaptures = []
        self.hangarcaptures = []
        self.totalgasincome = 0
        self.totalgasspent = 0
        self.alphasbuilt = 0
        self.strainpurchases = []
        self.upgradepurchases = []
        self.structurebuilt = 0
