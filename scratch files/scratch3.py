import sc2reader

path = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/Oh No It's Zombies Arctic Map (246).SC2Replay"
# path = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies Arctic Map (10).SC2Replay"

replay = sc2reader.load_replay(path, load_level=3)

eventlist = []
namedict = {}


for event in replay.events:
    if event.name == 'UnitDiedEvent':
        if event.frame > 573 and event.unit.name not in {'Marine', 'Marauder', 'DigesterCreepSprayUnit',
                                                        'HERC', 'Reaper', 'Ghost'}:
            if event.killer_pid is None and event.location != (255, 255):
                eventlist.append(event)
        # namedict.update({event.pid:event})
print(1)
print(2)

