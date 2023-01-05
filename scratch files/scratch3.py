import sc2reader
# from infodict import ultimateinfestationdict, t2alphadict

path = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/wonky replays/Oh_No_Its_Zombies_Arctic_Map_874.SC2Replay"
# path = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/presubmap/Oh No It's Zombies Arctic Updated (15).SC2Replay"
# path = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/presubmap/Oh_No_Its_Zombies_Arctic_Updated_128.SC2Replay"

# path = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies/Oh No It's Zombies Arctic Map (11).SC2Replay"

replay = sc2reader.load_replay(path, load_level=3)

print(1)

eventlist = []
namedict = {}
eventset = set()
# eventset2 = set()
# alphalist = []
# namelist = []
#
eventlist2 = []
# eventlist3 = []
# eventlist4 = []
# eventlist5 = []

# for human in replay.humans:
#     if human.play_race == 'Zerg':
#         for unit in human.units:
#             if unit.name is not None:
#                 eventlist.append(unit)
#                 eventset.add(unit.name)

for event in replay.events:
    # if event.name == 'UnitDoneEvent' and event.unit.owner.pid == 5:
    #     if event.unit.name not in {'AutoTurret', 'SensorTower'} and event.unit.killed_by is None:
    #         eventlist.append(event)
    # if event.name == 'UnitInitEvent'and event.unit_type_name == 'PsiIndoctrinator':
    #     eventlist.append(event)
    #     namelist.append(event.unit_type_name)
    # elif event.name == 'UnitOwnerChangeEvent' and event.unit.title == 'AutoTurret' and event.unit.type == 54:
    #     eventlist2.append(event)
    # if event.name == 'UnitTypeChangeEvent':
    #     if event.unit_type_name not in {'SpiderMine', 'SpiderMineBurrowed', 'Dehaka',
    #                                     'SentryGun', 'SpecOpsSentryGun', 'SentryGunUnderground', 'SpecOpsSentryGun2',
    #                                     'LabTurretUp', 'AutoTurret2',
    #                                     'InfestedTerranCampaignBurrowed', 'ToxicNestBurrowed',
    #                                     'InfestedExploder', 'Baneling', 'BanelingBurrowed', 'Kaboomer',
    #                                     'InfestedCivilian', 'InfestedCivilianBurrowed',
    #                                     'LocustMP', 'FlyingZombie', 'FlyingZombie2',
    #                                     'RoachCorpser', 'RoachCorpserBurrowed', 'RoachVile', 'DefilerMP',
    #                                     'InfestorTerran', 'DehakaMirrorImage', 'DehakaMirrorImageBurrowed',
    #                                     'Zergling', 'HotSRaptor', 'Hunterling', 'InfestedExploderBurrowed',
    #                                     'InfestorTerranBurrowed', 'Devastator', 'Devourer3', 'Mutalisk'}:
    #         if event.unit.owner is not None:
    #             eventlist.append(event)
    #             eventset.add(event.unit_type_name)
    # if event.name == 'UpgradeCompleteEvent':
    #     eventlist.append(event)
    #     eventset.add(event.upgrade_type_name)
    #     if event.pid > 7:
    #         eventlist2.append(event)
    #         eventset2.add(event.upgrade_type_name)
    if event.name == 'UnitBornEvent':
        if event.unit_type_name not in {'DigesterCreepSprayTargetUnit', 'DigesterCreepSprayUnit', 'NovaAcidPuddle2',
                                        'InfestedCivilian', 'LocustMP3',
                                        'InfestorTerran', 'InfestorTerranBurrowed',
                                        'DehakaMirrorImage', 'DehakaMirrorImageBurrowed',
                                        'InfestedExploder', 'Baneling', 'Kaboomer',
                                        'InfestedExploderBurrowed', 'BanelingBurrowed', 'Kaboomer2', 'AcidPuddle',
                                        'Zergling', 'HotSRaptor', 'HotSRaptorBurrowed', 'PureFastZombieLeaping',
                                        'RoachCorpser', 'RoachCorpserBurrowed', 'RoachVile',
                                        'ZergDropPod', 'CreepPod', 'FlyingZombie2',
                                        'Mutalisk', 'DevastatorLeaping', 'Devourer2', 'KerriganInfestBroodling',
                                        'ForceField', 'WarPig'}:
            if event.upkeep_pid is not None and event.upkeep_pid == 2:
                eventlist.append(event)
                eventset.add(event.unit_type_name)
            if event.unit_type_name in {'RoyalCocoon', 'QueenCoop'}:
                eventlist2.append(event)
    # if event.name == 'UnitTypeChangeEvent' and event.unit_type_name == 'MassiveCocoon':
    #     eventlist4.append(event)
print(eventset)
print(1)


# unitinitevent: 25
# eventlist: 41


# UpgradeCompleteEvent
# event.upgrade_type_name