import sc2reader

path = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies/Oh No It's Zombies Arctic Map (169).SC2Replay"
replay = sc2reader.load_replay(path, load_level=4)

print(replay)


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

Uninfested
Alpha	130	34078721	(50, 41)
Beta	128	33554433	(145, 234)
Delta	129	33816577	(215, 39)
'''

# https://pypi.org/project/sc2reader/
# https://sc2reader.readthedocs.io/en/latest/articles/creatingagameengineplugin.html
# https://github.com/ggtracker/sc2reader/tree/7da58b1e91e374f61bf2078319472eca8886c59a
# https://tl.net/forum/starcraft-2/545768-looking-for-a-replay-parser
# https://github.com/Blizzard/s2protocol