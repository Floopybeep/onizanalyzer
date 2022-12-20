import sc2reader

path = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/Oh No It's Zombies Arctic Map (245).SC2Replay"

replay = sc2reader.load_replay(path, load_level=3)

eventset = set()
checksets = {'UpgradeCompleteEvent', 'UnitBornEvent'}
eventlist = []

zergstat = None

def event_blacklist_check(event):
    UnitBornEventblacklist = {'InfestedCivilianBurrowed'}
    UpgradeCompleteEventblacklist = {'RefineryRoomInfestedExcavationZone', 'RefineryRoomInfestedManufacturingSector',
                                'RefineryRoomInfestedProcessingFacilities', 'RefineryRoomInfestedScienceLabs',
                                'VirophageroominfestedAlpha', 'VirophageroominfestedBeta', 'VirophageroominfestedDelta'}

    if event.frame == 0:
        return False
    if event.name == 'UnitBornEvent' and event.unit_type_name in UnitBornEventblacklist:
        return False
    elif event.name == 'UpgradeCompleteEvent' and event.upgrade_type_name in UpgradeCompleteEventblacklist:
        return False
    # elif event.name == 'UnitTypeChangeEvent':
    #     return False

    return True


for event in replay.events:
    if event_blacklist_check(event):
        if event.name == 'PlayerStatsEvent' and event.pid < 10 and event.player.play_race == 'Zerg':
            zergstat = event

        if event.name == 'UpgradeCompleteEvent':
            if event.upgrade_type_name not in {'LongRangeScope', 'FragGrenadeUnlocked', 'ExplorationDroidUnlocked',
                                               'TESTEquippedExplorationDroidUnlocked', 'MiningChargeUnlocked',
                                               'MotionSensorUnlocked', }:
                eventlist.append(event)

        # elif event.name == 'UnitBornEvent':
        #     if event.unit_type_name not in {'DigesterCreepSprayTargetUnit', 'DigesterCreepSprayUnit',
        #                                     'InfestedCivilian', 'InfestedExploder', 'Baneling', 'Kaboomer',
        #                                     'InfestedExploderBurrowed', 'BanelingBurrowed', 'LocustMP3',
        #                                     'InfestorTerran', 'DehakaMirrorImage', 'NovaAcidPuddle2',
        #                                     'PrimalTownHallUprooted', 'Kaboomer2', 'InfestorTerranBurrowed',
        #                                     'AcidPuddle', 'HotSRaptor', 'RoachCorpser',
        #                                     'ZergDropPod', 'CreepPod', 'DevastatorLeaping'}:
        #         if event.upkeep_pid != 10:
        #             eventlist.append(event)
        # elif event.name == 'UnitTypeChangeEvent':
        #     if event.unit_type_name not in {'SpiderMine', 'SpiderMineBurrowed', 'InfestedCivilian', 'SentryGun',
        #                                     'SpecOpsSentryGun', 'SentryGunUnderground', 'SpecOpsSentryGun2',
        #                                     'InfestedTerranCampaignBurrowed', 'LabTurretUp', 'AutoTurret2',
        #                                     'InfestedExploder', 'Baneling', 'Kaboomer', 'ToxicNestBurrowed'}:
        #         eventlist.append(event)

print(eventlist)

