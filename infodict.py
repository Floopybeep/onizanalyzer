upgradeeventset = {'UpgradeCompleteEvent', 'UnitTypeChangeEvent', 'UnitBornEvent', 'UnitInitEvent', 'PlayerStatsEvent'}

weapondict = {'FlamethrowerUnlocked': 10, 'ShotgunUnlocked': 11,
              'BeamRifleUnlocked': 13, 'HellfireRocketLauncherUnlocked': 14, 'ArcWelderUnlocked': 15,
              'AresUnlocked': 16, 'SpecOpsAresUnlocked': 26,
              'SpecOpsFlamethrower': 20, 'SpecOpsShotgun': 21, 'SpecOpsAssaultRifle': 22,
              'SpecOpsPlasmaRifle':23, 'SpecOpsHellfireRocketLauncher': 24, 'SpecOpsArcWelder': 25}
    #'AssaultRifleUnlocked': 12,

weaponmoddict = {'ThermiteFilamentsUnlocked': 1, 'CryoFreezeUnlocked': 2, 'LongRangeIncineratorsUnlocked': 3,
                 'HighPrecisionBeamsUnlocked': 11, 'ConcussiveShotUnlocked': 12, 'DoubleBarrelUnlocked': 13,
                 'AutoTargetingSystemUnlocked': 21, 'BayonetteUnlocked': 22, 'TitaniumBulletCasingsUnlocked': 23,
                 'CorrosivePlasmaUnlocked': 31, 'LongRangeScopeUnlocked': 32, 'ConcussivePlasmaUnlocked': 33,
                 'RocketLauncherMod1Unlocked': 41, 'ShockwaveMissilesUnlocked': 42, 'RocketLauncherMod3Unlocked': 43,
                 'ArcWelderMod1Unlocked': 51, 'ArcWelderMod2Unlocked': 52, 'ArcWelderMod3Unlocked': 53}

aresmoddict = {'AresMod1Unlocked': 0, 'AresMod2Unlocked': 1, 'AresMod3Unlocked': 2, 'AresMod4Unlocked': 3,
               'AresMod5Unlocked': 4, 'AresMod6Unlocked': 5, 'AresMod7Unlocked': 6, 'AresMod8Unlocked': 7,
               'AresMod9Unlocked': 8, 'AresMod10Unlocked': 9}

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
            'ShieldSiotUnlocked': 31, 'AdvancedShieldSuitUnlocked': 32}

structuredict = {'AutoTurretUnlocked': 0, 'HeavyTurretUnlocked': 1, 'SpecOpsTurretUnlocked': 2, 'FlameTurretUnlocked': 3,
                 'BioMechanicalRepairDroneUnlocked': 10, 'SpecOpsBioMechanicalRepairDroneUnlocked': 11,
                 'RechargeDroneUnlocked': 12, 'CombatAccelerationDroneUnlocked': 13,
                 'PsiDisrupterUnlocked': 20, 'PsiDepressorUnlocked': 21, 'SpecOpsPsiDisruptorUnlocked': 22}

miscset = {'CombatShieldUnlocked', 'MedicShieldUnlocked', 'EnergyPackUnlocked', 'QuantumBackpackUnlocked',
           'OpticalVisorUnlocked', 'AIAssistantUnlocked'}

experimentaldict = {'CloakingDeviceUnlocked': 0, 'SpecOpsCloakingDeviceUnlocked': 1,
                    'PowerConverterUnlocked': 10, 'SpecOpsPowerConverterUnlocked': 11,
                    'SuperStimpackUnlocked': 20, 'SpecOpsSuperStimpackUnlocked': 21,
                    'TeleporterUnlocked': 30, 'SpecOpsTeleporterUnlocked': 31,
                    'SuperHealingDroneUnlocked': 40, 'SpecOpsSuperHealingDroneUnlocked': 41,
                    'ArcWelderUnlocked': 50, 'SpecOpsArcWelder': 51,
                    'AresUnlocked': 60, 'SpecOpsAresUnlocked': 61}

experimentallist = ['Cloaking Device', 'Power Converter', 'Super Stimpack',
                    'Teleporter', 'Super Healing Drone', 'Arc Welder', 'ARES Tank']

structurecountset = {'AutoTurret', 'HealingDrone', 'PsiIndoctrinator'}

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

ultimateinfestationdict = {'SpawnHiveQueen': 'Hive Queen', 'CriticalMass': 'Critical Mass', 'BlackOut': 'Power Drain',
                           'NydusNetwork': 'Nydus Network', 'SweepingInfestation': 'Drop Pods'}

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
               3: 'Plasma', 4: 'Rocket', 5: 'Arc Welder', 6: 'ARES Tank'}
rweaponmodlist = [[None, 'Cryo', 'Range', 'Filaments'], [None, 'Focused Beams', 'Knockback', 'More in Wider'],
                  [None, 'Scoot-n-Shoot', 'Bayonette', 'Tits'], [None, 'Corrosive', 'Range', 'Slow'],
                  [None, 'Scoot-n-Shoot', 'Shockwave', 'Flame'], [None, 'Fastcharge', 'Fastsalv', 'Supercharge'],
                  [None, '']]

raresmoddict = {0: '', 1: '', 2: '',
                3: '', 4: '', 5: '',
                6: '', 7: '', 8: 'Hostile Treads', 9: ''}

rweaponmodshortdict = {0: '(F)', 1: '(S)', 2: '(AR)', 3: '(P)', 4: '(R)', 5: '(Arc)', 6: '(ARES)'}

rgrenadedict = {0: 'Force Field', 1: 'Flashbang', 2: 'Frag Grenade', 3: 'Incendiary'}

rminingdict = {0: 'Expo Droid', 1: 'Mining Droid', 2: 'Mining Charge', 3: 'Sensor Tower'}

raccessorydict = {0: 'Matrix', 1: 'Stimpack', 2: 'Overloader'}

rsuitdict = {0: 'HEV', 1: 'Accelerant', 2: 'Energy', 3: 'Shield'}

rmiscdict = {0: 'Medic Shield', 1: 'Combat Shield', 2: 'Quantum Pack', 3: 'Energy Pack', 4: 'Visor', 5: 'AI Assistant'}

rstructuredict = {0: 'Turret', 1: 'Heal Droid', 2: 'Psi Disruptor'}

rstructuremodlist = [[None, 'Heavy', 'SpecOps', 'Flame'], [None, 'SpecOps', 'Energy', 'Accel'], [None, 'Slow', 'SpecOps']]

rstructuremodshortdict = {0: '(T)', 1: '(HD)', 2: '(P)'}

ralphakillsdict = {0: 'Abberation', 1: 'Gene', 2: 'Anubalisk', 3: 'Legion', 4: 'Hunter', 5: 'Underseer'}

rzstructurekillsdict = {0: 'Sunken', 1: 'SwarmNest', 2: 'Creep Tower', 3: 'Lesser Nydus', 4: 'Extractor'}

############################################# Zombie Dict (reverse order) #############################################
rmajorroomdict = {0: 'Power', 1: 'FDC', 2: 'Containment', 3: 'Security', 4: 'Gates Control'}

rt1alphasdict = {0: 'Abberation', 1: 'Geneweaver', 2: 'Anubalisk', 3: 'Legion', 4: 'Hunter', 5: 'Underseer'}

rt2alphasdict = {0: 'Abomination', 1: 'Genesplicer', 2: 'Anubalight', 3: 'Legionnaire', 4: 'Predator', 5: 'Saboteur'}

rstrainsdict = {0: 'Speed Strain', 1: 'Health Strain', 2: 'Damage Strain', 3: 'Volatile Strain'}

rzupgradesdict = {0: 'Speed Creep', 1: 'Regen Creep', 2: 'Construction Creep', 3: 'Virulent Creep', 4: 'Drop Pods'}

rzadvupgradesdict = {0: 'Power Outage', 1: 'Siphon Gas', 2: 'Release Containment', 3: 'Chat Peek', 4: 'Door Closer'}

rhangardict = {0: 'Alpha', 1: 'Beta', 2: 'Delta'}

############################################## Bank dicts & Sets ######################################################
bankplayerdict = {'4:3AspectRatioSettings': 0, 'FuelDiverted': 0, 'GamesPlayedAsHuman': 0, 'GamesPlayedAsZombie': 0,
                  'HumanRank': 0, 'HumanWinsHard': 0, 'HumanWinsInsane': 0, 'HumanWinsNormal': 0, 'HumansCaptured': 0,
                  'HumansRescued': 0, 'IdleRally': 0, 'LeftLastGame': 0, 'NumberOfTimesCaptured': 0, 'ZombiesKilled': 0,
                  'SecurityForcesKilled': 0, 'TurretsBuilt': 0, 'VespeneHarvested': 0, 'ZombieRank': 0, 'ZombieWins': 0}

bankloaddict = {'Chosen_Zombie': 0, 'Color': 0, 'Difficulty': 0,
                'Experimental_Mode': 0, 'Host_Chooses_Zombie': 0, 'Opt_In': 0}

############################################## csv dict & sets ########################################################
total_df_human_column_list = ['Replay #', 'Replay Date', 'Player Name', 'Player Handle', 'Rank', 'Result', 'Weapon',
                              'Weapon Mod #1', 'Weapon Mod #2', 'Weapon Mod #3', 'Grenade', 'Scout Droid Upgrade',
                              'Mining Droid Upgrade', 'Nuke Upgrade', 'Sensor Upgrade', 'Accessory', 'Suits',
                              'Misc Shield Purchase', 'Misc Backpack Purchase', 'Misc Visor Purchase',
                              'Turret Bought', 'Heal Droid Bought', 'Psi Bought', 'Turret Mod',
                              'Heal Droid Mod', 'Psi Mod', 'Turrets Built', 'Heal Droids Built', 'Psis Built',
                              'Experimental', 'Kills', 'Deaths', 'Aberrations Killed', 'Abominations Killed',
                              'Geneweavers Killed', 'Genesplicers Killed', 'Anubalisks Killed', 'Anubalights Killed',
                              'Legions Killed', 'Legionnaires Killed', 'Hunters Killed', 'Predators Killed',
                              'Underseers Killed', 'Saboteurs Killed', 'Cocoons Killed', 'Structures Killed',
                              'Sunkens Killed', 'Swarmling Nests Killed', 'Creep Towers Killed', 'Lesser Nydus Killed',
                              'Extractors Killed']

total_df_zombie_column_list = ['Replay #', 'Replay Date', 'Player Name', 'Player Handle', 'Rank', 'Result',
                               'First Alpha', 'Abberations Built', 'Abominations Built', 'Geneweavers Built',
                               'Genesplicers Built', 'Anubalisks Built', 'Anubalights Built', 'Legions Built',
                               'Legionnaires Built', 'Hunters Built', 'Predators Built', 'Underseers Built',
                               'Saboteurs Built', 'No. of Alphas Built', 'T1 Speed Purchased', 'T2 Speed Purchased',
                               'T3 Speed Purchased', 'T1 Health Purchased', 'T2 Health Purchased', 'T3 Health Purchased',
                               'T1 Damage Purchased', 'T2 Damage Purchased', 'T3 Damage Purchased',
                               'T1 Volatile Purchased', 'T2 Volatile Purchased', 'T3 Volatile Purchased',
                               'Speed Creep Purchased', 'Regen Creep Purchased', 'Constructive Creep Purchased',
                               'Virulent Creep Purchased', 'Drop Pods Purchased', 'Drop Pods Used',
                               'Advanced Infestations', 'Ultimate Infestation', 'Sunkens Built', 'Swarmling Nests Built',
                               'Creep Towers Built', 'Lesser Nydus Built', 'Extractors Built', 'Greater Nydus Used',
                               'No. of Structures Built', 'Major Rooms Captured', 'Hangars Captured', 'Marines Captured',
                               'Cocoons Made', 'No. of Siphons']
