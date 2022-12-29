import s2protocol
import mpyq
from s2protocol import versions

reppath = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/wonky replays/Oh_No_Its_Zombies_Arctic_Map_874.SC2Replay"

archive = mpyq.MPQArchive(reppath)
print(archive.files)

protocol = versions.build(88500)

contents = archive.read_file('replay.game.events')
game_events = protocol.decode_replay_game_events(contents)
eventlist = []
eventnameset = set()

banksectionlist = []
bankkeylist = []
bankfilelist = []
banksignaturelist = []


for event in game_events:
    if event['_event'] not in eventnameset:
        eventnameset.add(event['_event'])
    if event['_event'] == 'NNet.Game.SBankSectionEvent':
        banksectionlist.append(event)
    elif event['_event'] == 'NNet.Game.SBankKeyEvent':
        bankkeylist.append(event)
    elif event['_event'] == 'NNet.Game.SBankFileEvent':
        bankfilelist.append(event)
    elif event['_event'] == 'NNet.Game.SBankSignatureEvent':
        banksignaturelist.append(event)

    # if event['_event'] in {'NNet.Game.SBankSectionEvent', 'NNet.Game.SBankKeyEvent',
    #                        'NNet.Game.SBankFileEvent', 'NNet.Game.SBankSignatureEvent'}:
    eventnameset.add(event['_event'])
    eventlist.append(event)

    # if event['_gameloop'] > 100:
    #     break

print(1)
print(1)

# NNet.Game.SBankKeyEvent

    # b'HumanWinsNormal'
    # b'ZombieRank'
    # b'VespeneHarvested'
    # b'HumansRescued'
    # b'SecurityForcesKilled'
    # b'ZombiesKilled'
    # b'FuelDiverted'
    # b'HumanWinsInsane'
    # b'LeftLastGame'
    # b'4:3AspectRatioSettings'
    # b'HumanRank'
    # b'IdleRally'
    # b'NumberOfTimesCaptured'
    # b'TurretsBuilt'
    # b'ZombieWins'
    # b'GamesLeft'
    # b'GamesPlayedAsHuman'
    # b'GamesPlayedAsZombie'
    # b'HumansCaptured'
    # b'HumanWinsHard'
    # b'Difficulty'
    # b'Opt In'
    # b'Color'
    # b'Chosen Zombie'
    # b'Host Chooses Zombie'
    # b'Experimental Mode'

# event[_event] == 'NNet.Game.SBankFileEvent' : load bank

# event[_event] == 'NNet.Game.SBankSectionEvent' : defines sub-section

    # b'Player'
    # b'Load'

# NNet.Game.SBankSignatureEvent : signs bank, change event['_m_signature'] to hexadcimal for signature
    # use hex(NUM).split('x')[-1] or format(number, 'x')




























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

def dropship_player_check(unit):
    if 188 <= unit.location[0] <= 211 and 212 <= unit.location[1] <= 255:
        return 1
    elif 212 <= unit.location[0] <= 235 and 212 <= unit.location[1] <= 255:
        return 2
    elif 236 <= unit.location[0] <= 256 and 212 <= unit.location[1] <= 255:
        return 3
    else:
        return False


# https://pypi.org/project/sc2reader/
# https://sc2reader.readthedocs.io/en/latest/articles/creatingagameengineplugin.html
# https://github.com/ggtracker/sc2reader/tree/7da58b1e91e374f61bf2078319472eca8886c59a
# https://tl.net/forum/starcraft-2/545768-looking-for-a-replay-parser
# https://github.com/Blizzard/s2protocol
