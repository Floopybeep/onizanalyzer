from infodict import *

class playerinfo():
    def __init__(self, name=None, pid=None, handle=None, role=None, victory=None, rank=0):
        self.playername = name
        self.pid = pid
        self.handle = handle
        self.playerrole = role
        self.victory = victory
        self.rank = rank


class marineinfo(playerinfo):
    def __init__(self, name, pid, handle, role, victory):
        super().__init__(name, pid, handle, role, victory)
        self.weapons = [[0, False, False, False] for _ in range(6)]             # weapon lv, respective mod levels
        self.grenades = [False for _ in range(4)]                               # grenade lv for respective grenade
        self.minings = [False for _ in range(4)]
        self.accessories = [False for _ in range(3)]
        self.suits = [False for _ in range(4)]
        self.miscs = [False for _ in range(6)]
        self.structures = [[False for _ in range(4)] for _ in range(3)]         # structure unlock, respective mod unlock
        self.experimental = 'None'

        self.kills = 0                      # done
        self.score = 0
        self.captures = 0                   # done
        self.saves = 0
        self.alphakills = [0, 0, 0, 0, 0, 0]        # done
        self.cocoonkills = 0                # done
        self.zstructurekills = [0, 0, 0, 0, 0]      # done
        self.explorationdroidsmade = 0      # done
        self.turretsbuilt = 0               # done
        self.repairdronesebuilt = 0         # done
        self.psisbuilt = 0                  # done
        self.totalgasincome = 0
        self.totalgasspent = 0
        self.dropshipfueledtime = None      # done

    def add_weapon(self, weapon=False, mod=False):
        if weapon:
            self.weapons[weapondict[weapon]%10][0] = weapondict[weapon]//10
        elif mod:
            self.weapons[weaponmoddict[mod]//10][weaponmoddict[mod]%10] = True

    def add_grenade(self, grenade):
        self.grenades[grenadedict[grenade]//10] = grenadedict[grenade]%10

    def add_mining(self, mining):
        self.minings[miningdict[mining]//10] = miningdict[mining]%10

    def add_accessories(self, accessory):
        if accessory == 'DefensiveMatrixUnlocked':  self.accessories[0] = True
        elif accessory == 'StimpackUnlocked':       self.accessories[1] = True
        else:                                       self.accessories[2] = True

    def add_suit(self, suit):
        self.suits[suitdict[suit]//10] = suitdict[suit]%10

    def add_structure(self, structure):
        self.structures[structuredict[structure]//10][structuredict[structure]%10] = True

    def add_misc(self, misc):
        if misc == 'CombatShieldUnlocked':      self.miscs[0] = True
        elif misc == 'MedicShieldUnlocked':     self.miscs[1] = True
        elif misc == 'EnergyPackUnlocked':      self.miscs[2] = True
        elif misc == 'QuantumBackpackUnlocked': self.miscs[3] = True
        elif misc == 'OpticalVisorUnlocked':    self.miscs[4] = True
        else:                                   self.miscs[5] = True

    def add_experimental(self, exp):
        result = ''
        if experimentaldict[exp]%10: result = 'Spec Ops '
        self.experimental = ''.join([result, experimentallist[experimentaldict[exp]//10]])

    def add_structurecounter(self, name):
        if name == 'TurretBuildCounter':        self.turretsbuilt += 1
        elif name == 'RepairDroneBuildCounter': self.repairdronesebuilt += 1
        else:                                   self.psisbuilt += 1


class zombieinfo(playerinfo):
    def __init__(self, name, pid, handle, role, victory):
        super().__init__(name, pid, handle, role, victory)
        self.majorroomcaptures = [False for _ in range(5)]              # Power, Fuel, Containment, Security, Gates
        self.alphasbuilt = [[0, 0] for _ in range(6)]                   # (Abom, Gene, Anub, Legion, Predator)(num)
        self.strainpurchases = [[0, 0, 0] for _ in range(4)]            # (Speed, Health, Damage, Volatile)(num)
        self.upgradepurchases = [0 for _ in range(5)]                   # (Speed, Regen, Constructive, Virulent, Pods)lv
        self.advancedinfestations = [False for _ in range(5)]           # Power, Fuel, Contain, Sec, Gates
        self.ultimateinfestation = None                                 # done
        self.infestationleveltimes = [None for _ in range(5)]           # time of inf levels

        self.hangarcaptures = [False for _ in range(3)]                 # Alpha, Beta, Delta
        self.structurebuiltlist = [0 for _ in range(5)]                  # Sunken, Broodling, Creep, LNydus, Extractor
        self.greaternydustimings = []

        self.startingalpha = None                   # done
        self.marinecaptures = 0                     # done
        self.cocoonsmade = 0                        # done
        self.cocoonids = set()
        self.droppodsused = 0                       # done
        self.roomcaptures = 0
        self.totalgasincome = 0
        self.totalgasspent = 0
        self.structurebuilt = 0                     # done
        self.siphons = 0                            # done

    # df = pd.DataFrame(columns=['Player Name', 'Handle', 'Result', 'Major Rooms Captured', 'Starting Alpha',
    #                                'Alphas Built', 'Strains Purchased', 'Upgrades Purchased', 'Advanced Infestations',
    #                                'Ultimate Infestatin', 'Hangars Captured', 'Structures Built',
    #                                'Infestation Level Timings', 'Greater Nydus Timings',
    #                                'Marine Captures', 'Cocoons Made', 'Drop Pods Used', 'Structures Built', 'Siphons'])
    def majorroom_capture(self, name):
        self.majorroomcaptures[majorroomdict[name]] = True

    def strain_purchase(self, name):
        self.strainpurchases[strainsdict[name]//10][strainsdict[name]%10] += 1

    def upgrade_purchase(self, name):
        self.upgradepurchases[zupgradesdict[name]] += 1

    def advancedinfestation_purchase(self, name):
        self.advancedinfestations[zadvancedinfestationsdict[name]] = True

    def infestationlevel_time(self, name, time):
        self.infestationleveltimes[infestationleveldict[name]] = time

    def ultimateinfestation_chosen(self, name):
        self.ultimateinfestation = ultimateinfestationdict[name]

    # UnitTypeChangeEvent
    def t2alpha_create(self, name):
        self.alphasbuilt[t2alphadict[name]][1] += 1

    def t1alpha_create(self, name):
        self.alphasbuilt[t1alphadict[name]][0] += 1

    def structure_create(self, name):
        self.structurebuiltlist[zstructuredict[name]] += 1

