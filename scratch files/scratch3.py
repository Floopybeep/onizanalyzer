import sc2reader

path = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/Oh No It's Zombies Arctic Map (245).SC2Replay"
# path = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies Arctic Map (10).SC2Replay"

replay = sc2reader.load_replay(path, load_level=3)

eventset = set()
checksets = {'UpgradeCompleteEvent', 'UnitBornEvent'}
eventlist = []
namelist = []

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

toxicnestcounter = 0

for event in replay.events:
    if event_blacklist_check(event):
        if event.name == 'UnitInitEvent':
            if event.unit_type_name not in {'MiningDroid', 'AutoTurret', 'SensorTower', 'PsiIndoctrinator',
                                            'NukePack', 'HealingDrone'}:
                eventlist.append(event)
                namelist.append(event.unit_type_name)
                if event.unit_type_name == 'ToxicNest':
                    toxicnestcounter += 1
print(1)
print(2)

