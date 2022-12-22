import sc2reader

# path = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/Oh No It's Zombies Arctic Map (246).SC2Replay"
path = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies/Oh No It's Zombies Arctic Map (11).SC2Replay"

replay = sc2reader.load_replay(path, load_level=3)

eventlist = []
namedict = {}
eventset = set()


for event in replay.events:
    if event.name == 'UpgradeCompleteEvent':
        if event.upgrade_type_name not in eventset:
            eventset.add(event.upgrade_type_name)
print(eventset)


