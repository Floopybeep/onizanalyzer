from infocondense import *


def append_replayinfo(replay, humandict, zombieplayer):
    out1 = append_humaninfo(replay, humandict)
    out2 = append_zombieinfo(replay, zombieplayer)
    return out1, out2


def bool_to_victory(booleandata):
    if booleandata:
        return "Win"
    else:
        return "Loss"


def bool_to_privpubs(booleandata):
    if booleandata:
        return "Private"
    else:
        return "Public"


def append_humaninfo(replay, humandict):
    outlist = []
    for key in humandict:
        human, data = humandict[key], {}
        data = {}

        data['Game ID'] = human.gameid
        data['Replay Date'] = str(replay.date)
        data['Player Name'] = human.playername
        data['Player Handle'] = human.handle
        data['Rank'] = human.rank
        data['Result'] = bool_to_victory(human.victory)
        data['Game Length'] = f"{replay.game_length.mins}.{replay.game_length.secs}"
        data['Private/Public'] = bool_to_privpubs(human.bankinfo.isprivate)
        data['Game Advantage'] = human.bankinfo.advantage
        data['Avg Human Rank'] = int(human.bankinfo.averagerank / 2 + 0.5)
        data['Weapon'] = hweaponfa(human.weapons)
        data['Weapon Mod #1'] = wmod(1, human.weapons)
        data['Weapon Mod #2'] = wmod(2, human.weapons)
        data['Weapon Mod #3'] = wmod(3, human.weapons)
        data['Grenade'] = hgrenadefa(human.grenades)
        data['Scout Droid Upgrade'] = miningmod(0, human.minings)
        data['Mining Droid Upgrade'] = miningmod(1, human.minings)
        data['Nuke Upgrade'] = miningmod(2, human.minings)
        data['Sensor Upgrade'] = miningmod(3, human.minings)
        data['Accessory'] = haccfa(human.accessories)
        data['Suits'] = hsuitfa(human.suits)
        data['Misc Shield Purchase'] = miscmod(0, human.miscs)
        data['Misc Backpack Purchase'] = miscmod(2, human.miscs)
        data['Misc Visor Purchase'] = miscmod(4, human.miscs)
        data['Turret Bought'] = human.structures[0][0]
        data['Heal Droid Bought'] = human.structures[1][0]
        data['Psi Bought'] = human.structures[2][0]
        data['Turret Mod'] = smod(0, human.structures)
        data['Heal Droid Mod'] = smod(1, human.structures)
        data['Psi Mod'] = smod(2, human.structures)
        data['Turrets Built'] = human.turretsbuilt
        data['Heal Droids Built'] = human.repairdronesebuilt
        data['Psis Built'] = human.psisbuilt
        data['Experimental'] = human.experimental
        data['Kills'] = human.kills
        data['Deaths'] = human.captures
        data['Aberrations Killed'] = human.alphakills[0][0]
        data['Abominations Killed'] = human.alphakills[0][1]
        data['Geneweavers Killed'] = human.alphakills[1][0]
        data['Genesplicers Killed'] = human.alphakills[1][1]
        data['Anubalisks Killed'] = human.alphakills[2][0]
        data['Anubalights Killed'] = human.alphakills[2][1]
        data['Legions Killed'] = human.alphakills[3][0]
        data['Legionnaires Killed'] = human.alphakills[3][1]
        data['Hunters Killed'] = human.alphakills[4][0]
        data['Predators Killed'] = human.alphakills[4][1]
        data['Underseers Killed'] = human.alphakills[5][0]
        data['Saboteurs Killed'] = human.alphakills[5][1]
        data['Cocoons Killed'] = human.cocoonkills
        data['Structures Killed'] = sum(human.zstructurekills)
        data['Sunkens Killed'] = human.zstructurekills[0]
        data['Swarmling Nests Killed'] = human.zstructurekills[1]
        data['Creep Towers Killed'] = human.zstructurekills[2]
        data['Lesser Nydus Killed'] = human.zstructurekills[3]
        data['Extractors Killed'] = human.zstructurekills[4]

        outlist.append(data)
        # total_replay_data.replays_data_human_list.append(data)
    return outlist


def hweaponfa(weaponlist):
    result = ''
    for i in range(7):
        if weaponlist[i][0] > 0:
            if len(result) > 0:
                result = result + ' & '
            result = ''.join([result, 'T', str(weaponlist[i][0]), ' ', rweapondict[i], ' '])

    return result

def hgrenadefa(grenadelist):
    result = ''
    for i in range(4):
        if grenadelist[i]:
            if len(result) > 0:
                result = result + ' & '
            result = ''.join([result, 'T', str(grenadelist[i]), ' ', rgrenadedict[i]])
    return result

def haccfa(acclist):
    result = ''
    for i in range(3):
        if acclist[i]:
            if len(result) > 0:
                result = result + ' & '
            result = ''.join([result, raccessorydict[i]])
    return result

def hsuitfa(suitlist):
    result = ''
    for i in range(4):
        if suitlist[i]:
            if len(result) > 0:
                result = result + ' & '
            result = ''.join([result, 'T', str(suitlist[i]), ' ', rsuitdict[i]])
    return result

def wmod(modnum, weaponlist):
    result = ''
    for i in range(7):
        if weaponlist[i][0] == 2:
            if weaponlist[i][modnum]:
                if len(result) > 0:
                    result = result + ' | '
                result = ''.join([result, rweaponmodshortdict[i], ': ', rweaponmodlist[i][modnum]])
    return result

def miningmod(modnum, mlist):
    if not mlist[modnum]:
        return 'None'
    else:
        return f"T{mlist[modnum]}"

def miscmod(modnum, mlist):
    modnum2 = modnum + 1
    if not (mlist[modnum] and mlist[modnum2]):
        return 'None'
    elif mlist[modnum] and mlist[modnum2]:
        return f"{rmiscdict[modnum]} and {rmiscdict[modnum2]}"
    elif mlist[modnum]:
        return f"{rmiscdict[modnum]}"
    else:
        return f"{rmiscdict[modnum2]}"

def smod(mn, slist):
    result = ''
    if not any(slist):
        return 'None'
    for i in range(1, 4):
        if slist[mn][i]:
            if len(result) > 0:
                result = result + ' & '
            result = ''.join([result, rstructuremodlist[mn][i]])
    return result

def append_zombieinfo(replay, zplayer):
    data = {}

    data['Game ID'] = zplayer.gameid
    data['Replay Date'] = str(replay.date)
    data['Player Name'] = zplayer.playername
    data['Player Handle'] = zplayer.handle
    data['Rank'] = zplayer.rank
    data['Result'] = bool_to_victory(zplayer.victory)
    data['Game Length'] = f"{replay.game_length.mins}.{replay.game_length.secs}"
    data['Private/Public'] = bool_to_privpubs(zplayer.bankinfo.isprivate)
    data['Game Advantage'] = zplayer.bankinfo.advantage
    data['Avg Human Rank'] = int(zplayer.bankinfo.averagerank / 2 + 0.5)
    data['First Alpha'] = zplayer.startingalpha
    data['Abberations Built'] = zplayer.alphasbuilt[0][0]
    data['Abominations Built'] = zplayer.alphasbuilt[0][1]
    data['Geneweavers Built'] = zplayer.alphasbuilt[1][0]
    data['Genesplicers Built'] = zplayer.alphasbuilt[1][1]
    data['Anubalisks Built'] = zplayer.alphasbuilt[2][0]
    data['Anubalights Built'] = zplayer.alphasbuilt[2][1]
    data['Legions Built'] = zplayer.alphasbuilt[3][0]
    data['Legionnaires Built'] = zplayer.alphasbuilt[3][1]
    data['Hunters Built'] = zplayer.alphasbuilt[4][0]
    data['Predators Built'] = zplayer.alphasbuilt[4][1]
    data['Underseers Built'] = zplayer.alphasbuilt[5][0]
    data['Saboteurs Built'] = zplayer.alphasbuilt[5][1]
    data['No. of Alphas Built'] = sum(sum(alist) for alist in zplayer.alphasbuilt)
    data['T1 Speed Purchased'] = zplayer.strainpurchases[0][0]
    data['T2 Speed Purchased'] = zplayer.strainpurchases[0][1]
    data['T3 Speed Purchased'] = zplayer.strainpurchases[0][2]
    data['T1 Health Purchased'] = zplayer.strainpurchases[1][0]
    data['T2 Health Purchased'] = zplayer.strainpurchases[1][1]
    data['T3 Health Purchased'] = zplayer.strainpurchases[1][2]
    data['T1 Damage Purchased'] = zplayer.strainpurchases[2][0]
    data['T2 Damage Purchased'] = zplayer.strainpurchases[2][1]
    data['T3 Damage Purchased'] = zplayer.strainpurchases[2][2]
    data['T1 Volatile Purchased'] = zplayer.strainpurchases[3][0]
    data['T2 Volatile Purchased'] = zplayer.strainpurchases[3][1]
    data['T3 Volatile Purchased'] = zplayer.strainpurchases[3][2]
    data['Speed Creep Purchased'] = zplayer.upgradepurchases[0]
    data['Regen Creep Purchased'] = zplayer.upgradepurchases[1]
    data['Constructive Creep Purchased'] = zplayer.upgradepurchases[2]
    data['Virulent Creep Purchased'] = zplayer.upgradepurchases[3]
    data['Drop Pods Purchased'] = zplayer.upgradepurchases[4]
    data['Drop Pods Used'] = zplayer.droppodsused
    data['Advanced Infestations'] = zadvinffa(zplayer.advancedinfestations)
    data['Ultimate Infestation'] = zplayer.ultimateinfestation
    data['Sunkens Built'] = zplayer.structurebuiltlist[0]
    data['Swarmling Nests Built'] = zplayer.structurebuiltlist[1]
    data['Creep Towers Built'] = zplayer.structurebuiltlist[2]
    data['Lesser Nydus Built'] = zplayer.structurebuiltlist[3]
    data['Extractors Built'] = zplayer.structurebuiltlist[4]
    data['Greater Nydus Used'] = len(zplayer.greaternydustimings)
    data['No. of Structures Built'] = sum(zplayer.structurebuiltlist)
    data['Major Rooms Captured'] = zmajorroomf(zplayer.majorroomcaptures)
    data['Hangars Captured'] = zhangarsfa(zplayer.hangarcaptures)
    data['Marines Captured'] = zplayer.marinecaptures
    data['Cocoons Made'] = zplayer.cocoonsmade
    data['No. of Siphons'] = zplayer.siphons

    # total_replay_data.replays_data_zombie_list.append(data)

    return data

def zadvinffa(alist):
    result = ''
    for i in range(5):
        if alist[i]:
            if len(result) > 0:
                result = result + ' & '
            result = ''.join([result, rzadvupgradesdict[i]])
    return result

def zhangarsfa(hlist):
    result = ''
    for i in range(3):
        if hlist[i]:
            if len(result) > 0:
                result = result + ' & '
            result = ''.join([result, rhangardict[i]])
    return result