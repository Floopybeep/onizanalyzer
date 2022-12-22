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
                    'SuperHealingDroneUnlocked': 40, 'SpecOpsSuperHealingDroneUnlocked': 41,
                    'ARESTANK': 50, 'SPECOPSARESTANK': 51}

experimentallist = ['Cloaking Device', 'Gas Converter', 'Super Stimpack',
                    'Teleporter', 'Super Healing Drone', 'ARES Tank']

structurecountset = {'TurretBuildCounter', 'RepairDroneBuildCounter', 'PsiDisruptorBuildCounter'}

########################################### Zerg Dicts & Sets ###################################################
# UpgradeCompleteEvent dicts
majorroomdict = {'PowerGeneratorInfested': 0, 'FuelDistributionInfested': 1, 'ContainmentInfested': 2,
                 'SecurityMainframeInfested': 3, 'GateControlInfested': 4}

strainsdict = {'StrainSpeed': 0, 'PureStrainSpeed': 1, 'HunterlingStrain': 2,
               'StrainHealth': 10, 'PureStrainHealth': 11, 'TankStrain': 12,
               'StrainDamage': 20, 'PureStrainDamage': 21, 'DefilerStrain': 22,
               'StrainVolatile': 30, 'PureStrainVolatile': 31, 'KaboomerStrain': 32}

zupgradesdict = {'CreepSpeed': 0, 'RegenerativeCreep': 1, 'ConstructiveCreep': 2, 'VirulentCreep': 3,
                 'UnlockDropPods': 4, 'EvolveDropPods': 4}

zadvancedinfestationsdict = {'UnknownUpgrade': 0, 'SiphonFuel': 1, 'AdvancedInfestationContainment': 2,
                             'AdvancedInfestationSecurity': 3, 'AdvancedInfestationGateControl': 4}

infestationleveldict = {'InfestationLevel2': 0, 'InfestationLevel3': 1, 'InfestationLevel4': 2,
                         'InfestationLevel5': 3, 'InfestationLevel6': 4}

ultimateinfestationdict = {'SpawnHiveQueen': 'Hive Queen', 'CriticalMass': 'Critical Mass',
                           'BlackOut': 'Power Drain', 'NydusNetwork': 'Nydus Network'}

# UnitTypeChangeEvent dicts
t2alphadict = {'Abomination': 0, 'GenesplicerUprooted': 1, 'Anubalight': 2, 'LegionnaireZombie': 3,
               'Predator2': 4, 'Saboteur': 5}

# UnitBornEvent dicts
t1alphadict = {'InfestedAbomination': 0, 'PrimalTownHallUprooted': 1, 'Anubalisk': 2, 'Lurker': 3,
               'Hunter': 4, 'Underseer': 5}

t1alphatonamedict = {'InfestedAbomination': 'Abberation', 'PrimalTownHallUprooted': 'Geneweaver',
                     'Anubalisk': 'Anubalisk', 'Lurker': 'Legion', 'Hunter': 'Hunter', 'Underseer': 'Underseer'}

# UnitInitEvent dicts
zstructuredict = {'PrimalSunkenColony': 0, 'LocustNest': 1, 'NydusCanalCreeper': 2, 'LesserNydusWorm': 3,
                  'AutomatedExtractor': 4}


class playerinfo():
    def __init__(self, name=None, pid=None, handle=None, role=None, victory=None):
        self.playername = name
        self.pid = pid
        self.handle = handle
        self.playerrole = role
        self.victory = victory


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
        self.experimental = None

        self.kills = 0
        self.score = 0
        self.captures = 0                   # done
        self.saves = 0
        self.alphakills = 0
        self.cocoonkills = 0
        self.zstructurekills = 0
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
        self.strainpurchases = [[0, 0, 0] for _ in range(4)]            # (Speed, Health, Damage, Volatile)(num)
        self.upgradepurchases = [0 for _ in range(5)]                   # (Speed, Regen, Constructive, Virulent, Pods)lv
        self.advancedinfestations = [False for _ in range(5)]           # Power, Fuel, Contain, Sec, Gates
        self.infestationleveltimes = [None for _ in range(5)]           # time of inf levels

        self.hangarcaptures = [False for _ in range(3)]                 # Alpha, Beta, Delta
        self.alphasbuilt = [[0, 0] for _ in range(6)]                   # (Abom, Gene, Anub, Legion, Predator)(num)
        self.structurebuiltist = [0 for _ in range(5)]                  # Sunken, Broodling, Creep, LNydus, Extractor
        self.greaternydustimings = []

        self.startingalpha = None                   # done
        self.ultimateinfestation = None             # done
        self.marinecaptures = 0                     # done
        self.cocoonsmade = 0                        # done
        self.cocoonids = set()
        self.droppodsused = 0                       # done
        self.roomcaptures = 0
        self.totalgasincome = 0                     # done
        self.totalgasspent = 0                      # done
        self.structurebuilt = 0                     # done
        self.siphons = 0                            # done

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
        self.structurebuiltist[zstructuredict[name]] += 1

