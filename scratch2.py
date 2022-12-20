import sc2reader
from os import listdir, walk
from os.path import isfile, join

folderpath = "C:/Users/USER/PycharmProjects/onizanalyzer/replays"
replaypaths = []


def dropship_player_check(unit):
    if 188 <= unit.location[0] <= 211 and 212 <= unit.location[1] <= 255:
        return 1
    elif 212 <= unit.location[0] <= 235 and 212 <= unit.location[1] <= 255:
        return 2
    elif 236 <= unit.location[0] <= 256 and 212 <= unit.location[1] <= 255:
        return 3
    else:
        return False


for path, subdirs, files in walk(folderpath):
    for name in files:
        if isfile(join(path, name)): replaypaths.append(join(path, name))

for replaypath in replaypaths:
    try:
        replay = sc2reader.load_replay(replaypath, load_level=3)
    except Exception:
        print("Replay corrupted, deleting replay: ", replaypath)
        pass

    print(1)




# totalcount = [0 for _ in range(7)]
# zBasicCommandEventlist = []
# print(1)
#
# for event in replay.game_events:
#     blacklist = {'UserOptionsEvent', 'CameraEvent', 'TargetPointCommandEvent', 'BasicCommandEvent',
#                  'SelectionEvent', 'GetControlGroupEvent', 'CommandManagerStateEvent',
#                  'UpdateTargetPointCommandEvent', 'UpdateTargetUnitCommandEvent', 'AddToControlGroupEvent',
#                  'ControlGroupEvent', 'PlayerLeaveEvent'}
#     if event.name not in blacklist:
#         totalcount[event.pid] += 1
#         if event.pid == 0:
#             zBasicCommandEventlist.append(event)

# print(1)

'''
How to determine winner?
Check if "~ hangar has been destroyed" has popped
maybe in message_events? 86, 93, 99
check players-Zplayer-killed_units-id 38010881(30,55)(A), 37486593(150,225)(B), 37748737(204,40)(D)
players-player-result = 'Win' (This is 'None' if the player leaves before victory screen)


If Z loses, dropships are not located (either destroyed or flew away)
If hangar control is destroyed, then dropship is destroyed.
    There is an indicator that tells you when the hangar control died.
If hangar control is not destroyed in time, then dropship lives and flies away
    Marines that lived will be inside the dropship (x,y positions available?)
    
Ideal Solution:
    There is evidence of dropship being destroyed (so that it can account for HC dying AFTER dropship leaves)
    
Solution:
1. Marines are at X, Y position for respective dropships (means they've won) (x, y over 190?)
2. 

Uninfested                              Ship Box
Alpha	130	34078721	(50, 41)        (188,212) ~ (211,255)
Beta	128	33554433	(145, 234)      (212,212) ~ (235,255)
Delta	129	33816577	(215, 39)       (236,212) ~ (256,255)
'''

# https://pypi.org/project/sc2reader/
# https://sc2reader.readthedocs.io/en/latest/articles/creatingagameengineplugin.html
# https://github.com/ggtracker/sc2reader/tree/7da58b1e91e374f61bf2078319472eca8886c59a
# https://tl.net/forum/starcraft-2/545768-looking-for-a-replay-parser
# https://github.com/Blizzard/s2protocol
