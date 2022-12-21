import sc2reader

path = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/Oh No It's Zombies Arctic Map (245).SC2Replay"
# path = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies Arctic Map (10).SC2Replay"

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
        if event.name == 'UpgradeCompleteEvent':
            if event.upgrade_type_name not in {'LongRangeScope', 'FragGrenadeUnlocked', 'ExplorationDroidUnlocked',
                                               'TESTEquippedExplorationDroidUnlocked', 'MiningChargeUnlocked',
                                               'MotionSensorUnlocked', }:
                if event.pid == 3:
                    eventlist.append(event)
print(1)
print(eventlist)

