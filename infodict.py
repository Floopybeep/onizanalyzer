weapondict = {'FlamethrowerUnlocked': 10, 'ShotgunUnlocked': 11, 'AssaultRifleUnlocked': 12,
              'BeamRifleUnlocked': 13, 'HellfireRocketLauncherUnlocked': 14, 'ArcWelderUnlocked': 15,
              'SpecOpsFlamethrower': 20, 'SpecOpsShotgun': 21, 'SpecOpsAssaultRifle': 22,
              'SpecOpsPlasmaRifle':23, 'SpecOpsHellfireRocketLauncher': 24, 'SpecOpsArcWelder': 25}

weaponmoddict = {'ThermiteFilamentsUnlocked': 1, 'CryoFreezeUnlocked': 2, 'LongRangeIncineratorsUnlocked': 3,
                 'HighPrecisionBeamsUnlocked': 11, 'ConcussiveShotUnlocked': 12, 'DoubleBarrelUnlocked': 13,
                 'AutoTargetingSystemUnlocked': 21, 'BayonetteUnlocked': 22, 'TitaniumBulletCasingsUnlocked': 23,
                 'CorrosivePlasmaUnlocked': 31, 'LongRangeScopeUnlocked': 32, 'ConcussivePlasmaUnlocked': 33,
                 'RocketLauncherMod1Unlocked': 41, 'ShockwaveMissilesUnlocked': 42, 'RocketLauncherMod3Unlocked': 43,
                 'ArcWelderMod1Unlocked': 51, 'ArcWelderMod2Unlocked': 52, 'ArcWelderMod3Unlocked': 53}

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

################################################### Human Equip Dict (reverse order) ##################################
rweapondict = {0: 'Flamethrower', 1: 'Shotgun', 2: 'Assault Rifle',
               3: 'Plasma', 4: 'Rocket', 5: 'Arc Welder'}
rweaponmodlist = [[None, 'Cryo', 'Range', 'Filaments'], [None, 'Focused Beams', 'Knockback', 'More in Wider'],
                  [None, 'Scoot-n-Shoot', 'Bayonette', 'Tits'], [None, 'Corrosive', 'Range', 'Slow'],
                  [None, 'Scoot-n-Shoot', 'Shockwave', 'Flame'], [None, 'Fastcharge', 'Fastsalv', 'Supercharge']]

rweaponmodshortdict = {0: '(F)', 1: '(S)', 2: '(AR)', 3: '(P)', 4: '(R)', 5: '(Arc)'}

rgrenadedict = {0: 'Force Field', 1: 'Flashbang', 2: 'Frag Grenade', 3: 'Incendiary'}

rminingdict = {0: 'Expo Droid', 1: 'Mining Droid', 2: 'Mining Charge', 3: 'Sensor Tower'}

raccessorydict = {0: 'Matrix', 1: 'Stimpack', 2: 'Overloader'}

rsuitdict = {0: 'HEV', 1: 'Accelerant', 2: 'Energy', 3: 'Shield'}

rmiscdict = {0: 'Medic Shield', 1: 'Combat Shield', 2: 'Quantum Pack', 3: 'Energy Pack', 4: 'Visor', 5: 'AI Assistant'}

rstructuredict = {0: 'Turret', 1: 'Heal Droid', 2: 'Psi Disruptor'}

rstructuremodlist = [[None, 'Heavy', 'SpecOps', 'Flame'], [None, 'SpecOps', 'Accel', 'Energy'], [None, 'Slow', 'SpecOps']]

ralphakillsdict = {0: 'Abberation', 1: 'Gene', 2: 'Anubalisk', 3: 'Legion', 4: 'Hunter', 5: 'Underseer'}

rzstructurekillsdict = {0: 'Sunken', 1: 'SwarmNest', 2: 'Creep Tower', 3: 'Lesser Nydus', 4: 'Extractor'}

############################################# Zombie Dict (reverse order) #############################################
rmajorroomdict = {0: 'Power', 1: 'FDC', 2: 'Containment', 3: 'Security', 4: 'Gates Control'}

rt2alphasdict = {0: 'Abomination', 1: 'Genesplicer', 2: 'Anubalight', 3: 'Legionnaire', 4: 'Predator', 5: 'Saboteur'}

rstrainsdict = {0: 'Speed Strain', 1: 'Health Strain', 2: 'Damage Strain', 3: 'Volatile Strain'}

rzupgradesdict = {0: 'Speed Creep', 1: 'Regen Creep', 2: 'Construction Creep', 3: 'Virulent Creep', 4: 'Drop Pods'}

rzadvupgradesdict = {0: 'Power Outage', 1: 'Siphon Gas', 2: 'Release Containment', 3: 'Chat Peek', 4: 'Door Closer'}

rhangardict = {0: 'Alpha', 1: 'Beta', 2: 'Delta'}
