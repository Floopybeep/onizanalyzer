'''
Current Plan
1. (Done) Take all replays from a folder (including subfolders) using the beginning of scratch_dupcheck
2. For each replay, analyze info and store in corresponding subclass in infoextract (playerinfo - marineinfo/zombieinfo)
    2.1. Create a text file that includes information from 2?
         Date, Players(+PIDs), Game Length, Average Rank, etc...
    2.2. Store info in a separate array/list?
    2.3. Extract banks for each player, and store in separate list.
        2.3.1. If collision is detected, then overwrite for the latest replay
3. Save banks from 2.3. in a separate folder
4. Create statistics using information in 3

5. Create a UI to wrap the program around (including input, save location, etc...)
6. Make a discord bot down the line...
'''

'''
Feature List
- turns replays to text documents
- comparison
- rankings
- grabs most recent banks for comparsion
- Top 50 marines for... kills, wins, win %, etc.
- Win % for guns, # nukes, etc....
- Extract Banks

What's in the Replay object?
- date (2022-11-03 02:16:15)
- start_time (2022-11-03 02:01:18)
- end_time (2022-11-03 02:16:15)
- entities (list)
    -
- events (list, super long)
    - PlayerSetupEvent
    - UnitBornEvent
- game_events (list)
- game_length (14.57)

- humans (list) (human is dict)
    - 0, 1, 2...
        - events (ProgressEvent, UserOptionsEvent, CameraEvent)
- messages (list)
- message_events (list)

- packets
- people (list)
    - 0: Player
    - 1: Security

- raw_data (dict)
    - replay.initData.backup
    - replay.details.backup
    - replay.attributes.events
    - replay.initData
    - replay.details
    - replay.message.events
    - replay.tracker.events
    - replay.game.events

- real_length (14.57)
- team (dict)
- teams (list)
'''

'''
Output file format
1. text file summary for each game
game ID - to prevent re-analysis of game (00000001 - eight-digit format, one for each?) (maybe make unique identifier?)

2. Players
ProDem       Zerg    16
ToxicPanda   Terran  12 ....

3. Zombie/Human Victory

4. Detailed Information (Tabular Format)
4-1. Human Info
Players     UID         Kills       Saves       Deaths      Gas Earned      Gas Spent       Weapon Used     Experimental
Alany       S1-1-...    

4-2. Zombie Info
Player      UID         Captures    Self-Breaks     Alphas Created      Strains Purchased       Ultimate Infestation



4-1.
Player Name, UID, Kills, Saves, Deaths, Gas Earned, Gas Spent, Weapon Used, Experimental, Score, Alphas Killed, Diverts,
Number of Psis Placed, Weapon Modification Purchased, Nukes Placed, Suit Purchased, Total Upgrades

4-2.
Player Name, UID, Captures, Self-Breaks, Alphas Created, Strains Purchased, Ultimate Infestation, Major Rooms Infested,
Number of Rooms Infested, Hangars Captured, Upgrades Purchased, Advanced Infestations
'''
# possible candidate for unique identifier:
#   game length
#   players in game
#   zombie chosen
#   date - surefire method if all replays are from the same player
#   first five chatevents

#   Maybe just use filehash? It's available in lv=2 ('d8eb9f9e9e0482a01ab4e8b397a572dc29d38d5a6a8e7e282b9027ff9165056e')
