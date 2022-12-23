import time
from infodict import *

def log(text, logger_file):
    with open(logger_file, 'a') as f:
        f.write(text)
        f.close()

def bool_to_victory(booleandata):
    if booleandata:
        return "Win"
    else:
        return "Loss"

def set_replay_name(replay, humanlist, zplayer):
    date = replay.date
    replaytime = ''.join(['[', ' '.join(['-'.join([str(date.year), str(date.month), str(date.day)]),
                           '.'.join([str(date.hour), str(date.minute), str(date.second)])]), ']'])
    if zplayer.victory: whowins = '(Zwin)'
    else: whowins = '(Hwin)'

    playernames = ', '.join([zplayer.playername, ', '.join([player.playername for player in humanlist])])
    textfilename = ' - '.join([replaytime, whowins, playernames, '.txt'])

    return textfilename

def condense_eventinfo(replay, txtpath, humandict, zplayer):
    humanlist = [humandict[m] for m in humandict]
    name = set_replay_name(replay, humanlist, zplayer)
    txtpath = '/'.join([txtpath, name])

    with open(txtpath, 'w') as f:
        f.write(f"Date: {replay.date}\n")
        f.write(f"Game Length: {replay.game_length.mins}.{replay.game_length.secs}\n\n")

        f.write("Players\n")
        f.write('Player Name\tRole\t\tRank\tVictory\n')
        f.write('{0:15}\t{1:6}\t\t{2:4}\t{3}\n'.format(zplayer.playername, zplayer.playerrole, zplayer.rank, bool_to_victory(zplayer.victory)))
        for hplayer in humanlist:
            f.write('{0:15}\t{1:5}\t\t{2:4}\t{3}\n'.format(hplayer.playername, hplayer.playerrole, hplayer.rank, bool_to_victory(hplayer.victory)))
        f.write("\n\n")
        if zplayer.victory:
            f.write("Zombie victory\n")
        else:
            f.write("Human victory\n")

        humaninfocondense(humandict, f)
        zombieinfocondense(zplayer, f)

        f.close()

def humaninfocondense(humandict, f):
    f.write('Player Name\tHandle\tResult\tWeapons Used\tMod Used\tGrenades Used\tMining Equipment\n')
    for key in humandict:
        human = humandict[key]
        f.write('{0:15}\t{1:14}\t{2:4}\t{3:13}\t{4:13}\t{5:14}\t{6:15}\n'.format(human.playername, human.handle,
                bool_to_victory(human.victory), hweaponf(human.weapons), hwmodf(human.weapons),
                hgrenadef(human.grenades), hminingf(human.minings)))

    f.write('\nWeapon Accessories\tSuits\tMisc Items\tStructures Purchased\tStructure Mods\tExperimental Used\n')
    for key in humandict:
        human = humandict[key]
        f.write('{0:15}\t{1:13}\t{2:12}\t{3:13}\t{4:7}\t{4:19}\n'.format(
            haccf(human.accessories), hsuitf(human.suits), hmiscf(human.miscs), hstructuref(human.structures),
            hstructmodf(human.structures), human.experimental
        ))

    # What if player bought heavy and flame turrets, AND spec ops psi? it will show heavy, flame, specops... fix to heavy, flame turret, spec ops psi
    # Also fix char length for multiple purchases

def hweaponf(weaponlist):
    result = ''
    for i in range(6):
        if weaponlist[i][0] > 0:
            if len(result) > 0:
                result = result + ', '
            ''.join([result, 'T', str(weaponlist[i][0]), ' ', rweapondict[i], ' '])

    return result

def hwmodf(weaponlist):
    result = ''
    for i in range(6):
        for j in range(1, 4):
            if weaponlist[i][j]:
                if len(result) > 0:
                    result = result + ', '
                ''.join([result, rweaponmodlist[i][j]])
    return result

def hgrenadef(grenadelist):
    result = ''
    for i in range(4):
        if grenadelist[i]:
            if len(result) > 0:
                result = result + ', '
            ''.join([result, 'T', grenadelist[i], ' ', rgrenadedict[i]])
    return result

def hminingf(mininglist):
    result = ''
    for i in range(4):
        if mininglist[i]:
            if len(result) > 0:
                result = result + ', '
            ''.join([result, 'T', mininglist[i], ' ', rminingdict[i]])
    return result

def haccf(acclist):
    result = ''
    for i in range(3):
        if acclist[i]:
            if len(result) > 0:
                result = result + ', '
            ''.join([result, raccessorydict[i]])
    return result

def hsuitf(suitlist):
    result = ''
    for i in range(4):
        if suitlist[i]:
            if len(result) > 0:
                result = result + ', '
            ''.join([result, 'T', suitlist[i], ' ', rsuitdict[i]])
    return result

def hmiscf(misclist):
    result = ''
    for i in range(6):
        if misclist[i]:
            if len(result) > 0:
                result = result + ', '
            ''.join([result, rmiscdict[i]])
    return result

def hstructuref(structlist):
    result = ''
    for i in range(3):
        if structlist[i]:
            if len(result) > 0:
                result = result + ', '
            ''.join([result, rstructuredict[i], ' '])
    return result

def hstructmodf(structlist):
    result = ''
    for i in range(3):
        for j in range(1, 4):
            if structlist[i][j]:
                if len(result) > 0:
                    result = result + ', '
                ''.join([result, rstructuremodlist[i][j]])
    return result

def halphakillf(akilllist):
    result = ''
    for i in range(6):
        if akilllist[i]:
            if len(result) > 0:
                result = result + ', '
            ''.join([result, akilllist[i], ' ', ralphakillsdict[i]])
    return result

def hzstructkillf(zkilllist):
    result = ''
    for i in range(5):
        if zkilllist[i]:
            if len(result) > 0:
                result = result + ', '
            ''.join([result, zkilllist[i], ' ', zstructuredict[i]])
    return result

def zombieinfocondense(zplayer, f):
