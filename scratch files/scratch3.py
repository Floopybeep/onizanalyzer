import sc2reader
from infodict import ultimateinfestationdict

path = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/Oh No It's Zombies Arctic Map (252).SC2Replay"
# path = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies/Oh No It's Zombies Arctic Map (11).SC2Replay"

replay = sc2reader.load_replay(path, load_level=3)

eventlist = []
namedict = {}
eventset = set()
alphalist = []
namelist = []


for event in replay.events:
    # if event.name == 'UpgradeCompleteEvent' and event.pid not in {1, 2, 3, 4, 5, 6, 7}:
    if event.name == 'UnitBornEvent'and event.unit_type_name == 'MassiveCocoon':
        eventlist.append(event)
        namelist.append(event.unit_type_name)
        # eventset.add(event.upgrade_type_name)
print(eventset)
print(1)


# unitinitevent: 25
# eventlist: 41


# UpgradeCompleteEvent
# event.upgrade_type_name