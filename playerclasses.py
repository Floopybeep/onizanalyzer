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

weapondict = {'FlamethrowerUnlocked': 10, 'ShotgunUnlocked': 11, 'AssaultRifleUnlocked': 12,
              'BeamRifleUnlocked': 13, 'HellfireRocketLauncherUnlocked': 14, 'ArcWelderUnlocked': 15,
              'SpecOpsFlamethrower': 20, 'SpecOpsShotgun': 21, 'SpecOpsAssaultRifle': 22,
              'SpecOpsPlasmaRifle':23, 'SpecOpsHellfireRocketLauncher': 24, 'SpecOpsArcWelder': 25}

weaponmoddict = {'ThermiteFilamentsUnlocked': 1, 'CryoFreezeUnlocked': 2, 'LongRangeIncineratorsUnlocked': 3,
                 'HighPrecisionBeamsUnlocked': 11, 'ConcussiveShotUnlocked': 12, 'DoubleBarrelUnlocked': 13,
                 'AutoTargetingSystemUnlocked': 21, 'BayonetteUnlocked': 22, 'TitaniumBulletCasingsUnlocked': 23,
                 'CorrosivePlasmaUnlocked': 31, 'LongRangeScopeUnlocked': 32, 'ConcussivePlasmaUnlocked': 33,
                 'RocketLauncherMod1Unlocked': 41, 'ShockwaveMissilesUnlocked': 42, 'RocketLauncherMod3Unlocked': 43,
                 'ArcWelderMod1': 51, 'ArcWelderMod2': 52, 'ArcWelderMod3': 53}

grenadedict = {'ForceFieldGrenadeUnlocked': 1, 'SpecOpsForcefieldGrenade': 2,
               'FlashbangUnlocked': 11, 'SpecOpsFlashbang': 12,
               'FragGrenadeUnlocked': 21, 'SpecOpsFragGrenade': 22,
               'IncendiaryGrenadeUnlocked': 31, 'SpecOpsIncendiaryGrenade': 32}

miningdict = {'ExplorationDroidUnlocked': 1, 'TESTEquippedExplorationDroidUnlocked': 2,
              'MiningDroidUnlocked': 11, 'AdvancedDroidEngines': 12, 'TurboDroidEngines': 13,
              'MiningChargeUnlocked': 21, 'AdvancedMiningCharge': 22,
              'MotionSensorUnlocked': 31, 'AdvancedMotionSensor': 32}

accessoryset = {'DefensiveMatrixUnlocked', 'StimpackUnlocked', 'OverloadWeaponUnlocked'}

suitdict = {'HazmatSuitUnlocked': 1, 'AdvancedHazmatSuitUnlocked': 2,
            'EnergySuitUnlocked': 11, 'AdvancedEnergySuitUnlocked': 12,
            'CombatSuitUnlocked': 21, 'AdvancedCombatSuitUnlocked': 22,
            'ShieldSuitUnlocked': 31, 'AdvancedShieldSuitUnlocked': 32}

structuredict = {'AutoTurretUnlocked': 0, 'HeavyTurretUnlocked': 1, 'SpecOpsTurretUnlocked': 2, 'FlameTurretUnlocked': 3,
                 'BioMechanicalRepairDroneUnlocked': 10, 'SpecOpsBioMechanicalRepairDroneUnlocked': 11,
                 'RechargeDroneUnlocked': 12, 'CombatAccelerationDroneUnlocked': 13,
                 'PsiDisruptorUnlocked': 20, 'PsiDepressorUnlocked': 21, 'SpecOpsPsiDisruptorUnlocked': 22}

miscset = {'CombatShieldUnlocked', 'MedicShieldUnlocked', 'EnergyPackUnlocked', 'QuantumBackpackUnlocked',
           'OpticalVisorUnlocked', 'AIAssistantUnlocked'}

experimentaldict = {'CloakingDeviceUnlocked': 0, 'SpecOpsCloakingDeviceUnlocked': 1,
                    'GASCOVNERTER': 10, 'SPECOPSGASCONVERTER': 11,
                    'SuperStimpackUnlocked': 20, 'SPECOPSSUPERSTIM': 21,
                    'TeleporterUnlocked': 30, 'SpecOpsTeleporterUnlocked': 31,
                    'SuperHealingDroneUnlocked':40, 'SpecOpsSuperHealingDroneUnlocked': 41,
                    'ARESTANK': 50, 'SPECOPSARESTANK': 51}

experimentallist = ['Cloaking Device', 'Gas Converter', 'Super Stimpack',
                    'Teleporter', 'Super Healing Drone', 'ARES Tank']

structurecountset = {'TurretBuildCounter', 'RepairDroneBuildCounter', 'PsiDisruptorBuildCounter'}


class playerinfo():
    def __init__(self, name, pid, handle, role, victory):
        self.playername = name
        self.pid = pid
        self.handle = handle
        self.playerrole = role
        self.victory = victory


class marineinfo(playerinfo):
    def __init__(self, name, pid, handle, role, victory):
        super().__init__(name, pid, handle, role, victory)
        self.weapons = [[0, False, False, False] for _ in range(6)]             # weapon lv, respective mod levels
        self.grenades = [False for _ in range(4)]                                   # grenade lv for respective grenade
        self.minings = [False for _ in range(4)]
        self.accessories = [False for _ in range(3)]
        self.suits = [False for _ in range(4)]
        self.miscs = [False for _ in range(6)]
        self.structures = [[False for _ in range(4)] for _ in range(3)]         # structure unlock, respective mod unlock
        self.experimental = None

        self.kills = 0
        self.score = 0
        self.captures = 0
        self.saves = 0
        self.alphakills = 0
        self.cocoonkills = 0
        self.zstructurekills = 0
        self.turretsbuilt = 0
        self.repairdronesebuilt = 0
        self.psisbuilt = 0
        self.totalgasincome = 0
        self.totalgasspent = 0

    def add_weapon(self, weapon=False, mod=False):
        if weapon:
            self.weapons[weapondict[weapon]%10][0] = weapondict[weapon]/10
        elif mod:
            self.weapons[weaponmoddict[mod]/10][weaponmoddict[mod]%10] = True

    def add_grenade(self, grenade):
        self.grenades[grenadedict[grenade]/10] = grenadedict[grenade]%10

    def add_mining(self, mining):
        self.minings[miningdict[mining]/10] = miningdict[mining]%10

    def add_accessories(self, accessory):
        if accessory == 'DefensiveMatrixUnlocked':  self.accessories[0] = True
        elif accessory == 'StimpackUnlocked':       self.accessories[1] = True
        else:                                       self.accessories[2] = True

    def add_suit(self, suit):
        self.suits[suitdict[suit]/10] = suitdict[suit]%10

    def add_structure(self, structure):
        self.structures[structuredict[structure]/10][structuredict[structure]%10] = True

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
        self.experimental = ''.join([result, experimentallist[experimentaldict[exp]/10]])

    def add_structurecounter(self, name):
        if name == 'TurretBuildCounter':        self.turretsbuilt += 1
        elif name == 'RepairDroneBuildCounter': self.repairdronesebuilt += 1
        else:                                   self.psisbuilt += 1


class zombieinfo(playerinfo):
    def __init__(self, name, pid, handle, role, victory):
        super().__init__(name, pid, handle, role, victory)
        self.marinecaptures = 0
        self.roomcaptures = 0
        self.majorroomcaptures = [False, False, False, False, False]    # Power, Fuel, Containment, Security, Gates
        self.hangarcaptures = [False, False, False]                     # Alpha, Beta, Delta
        self.totalgasincome = 0
        self.totalgasspent = 0
        self.alphasbuilt = [[0, 0] for _ in range(5)]                   # [Type][Tiers], Type = (Abom, Gene, Anub, Legion, Predator)
        self.startingalpha = None
        self.strainpurchases = [[0, 0, 0] for _ in range(4)]            # [Strain][Tiers], Strains = (Speed, Health, Damage, Volatile)
        self.upgradepurchases = [[0, 0] for _ in range(4)]              # [Type][Tiers], Type = (Speed, Regen, Constructive, Virulent)
        self.structurebuilt = 0
        self.siphons = 0