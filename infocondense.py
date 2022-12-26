import datetime
from infodict import *
# import pandas as pd
import tabulate
from prettytable import *

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
    # pd.set_option('display.max_colwidth', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', 2000)
    # pd.set_option("expand_frame_repr", False) # print cols side by side as it's supposed to be

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
            f.write("Zombie victory\n\n\n")
        else:
            f.write("Human victory\n\n\n")

        f.write("Detailed Analysis - Humans\n")

        humaninfocondense(humandict, txtpath, f)

        f.write("\nDetailed Analysis - Zombie\n")
        zombieinfocondense(zplayer, txtpath, f)

        f.close()

def humaninfocondense(humandict, txtpath, f):
    # df = pd.DataFrame(columns=['Player Name', 'Handle', 'Result', 'Weapons Used', 'Mod Used', 'Grenades Used',
    #                                'Mining Equipment', 'Weapon Accessory', 'Suits Used', 'Misc Items', 'Structures',
    #                                'Structure Mods', 'Experimental', 'Total Kills', 'Deaths', 'Cocoons Killed',
    #                                'Alphas Killed', 'Zerg Structures Killed', 'Explo Droids Made',
    #                                'Turrets Built', 'Repair Drones Built', 'Psis Built', 'Dropship Fueling Time'])
    tab = PrettyTable()
    tab.field_names = ['Player Name', 'Handle', 'Result', 'Weapons Used', 'Mod Used', 'Grenades Used',
                                   'Mining Equipment', 'Weapon Accessory', 'Suits Used', 'Misc Items', 'Structures',
                                   'Structure Mods', 'Experimental', 'Total Kills', 'Deaths', 'Cocoons Killed',
                                   'Alphas Killed', 'Zerg Structures Killed', 'Explo Droids Made',
                                   'Turrets Built', 'Repair Drones Built', 'Psis Built', 'Dropship Fueling Time']

    for key in humandict:
        human = humandict[key]
        data = {}
        data['Player Name'] = human.playername
        data['Handle'] = human.handle
        data['Result'] = bool_to_victory(human.victory)
        data['Weapons Used'] = hweaponf(human.weapons)
        data['Mod Used'] = hwmodf(human.weapons)
        data['Grenades Used'] = hgrenadef(human.grenades)
        data['Mining Equipment'] = hminingf(human.minings)
        data['Weapon Accessory'] = haccf(human.accessories)
        data['Suits Used'] = hsuitf(human.suits)
        data['Misc Items'] = hmiscf(human.miscs)
        data['Structures'] = hstructuref(human.structures)
        data['Structure Mods'] = hstructmodf(human.structures)
        data['Experimental'] = human.experimental
        data['Total Kills'] = human.kills
        data['Deaths'] = human.captures
        data['Cocoons Killed'] = human.cocoonkills
        data['Alphas Killed'] = halphakillf(human.alphakills)
        data['Zerg Structures Killed'] = hzstructkillf(human.zstructurekills)
        data['Explo Droids Made'] = human.explorationdroidsmade
        data['Turrets Built'] = human.turretsbuilt
        data['Repair Drones Built'] = human.repairdronesebuilt
        data['Psis Built'] = human.psisbuilt
        data['Fueling Time'] = human.dropshipfueledtime

        # df = pd.concat([df, pd.DataFrame(data, index=[0])])
        tab.add_row(list(data.values()))

    # tabulate.PRESERVE_WHITESPACE = True
    # with open("C:/Users/USER/PycharmProjects/onizanalyzer/replays/text file output/asdf.txt", 'a') as f:
        # f.write(tabulate.tabulate(df, headers='keys', showindex=False, tablefmt="presto", colalign="right"))
        # print(tabulate.tabulate(df), file=f)
    tab.align = "l"
    tabstring = tab.get_string()
    print(tabstring, file=f)

    # df.to_csv(txtpath, sep='\t', index=False, header=False, encoding='ascii', mode='a')       # save df to diff file?


    # What if player bought heavy and flame turrets, AND spec ops psi? it will show heavy, flame, specops... fix to heavy, flame turret, spec ops psi

def hweaponf(weaponlist):
    result = ''
    for i in range(6):
        if weaponlist[i][0] > 0:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, 'T', str(weaponlist[i][0]), ' ', rweapondict[i], ' '])

    return result

def hwmodf(weaponlist):
    result = ''
    for i in range(6):
        if any(weaponlist[i][1:]):
            if len(result) > 0:
                result = result + '/ '
            result = ''.join([result, rweaponmodshortdict[i], ': '])
        for j in range(1, 4):
            if weaponlist[i][j]:
                if len(result) > 7:
                    result = result + ', '
                result = ''.join([result, rweaponmodlist[i][j]])
    return result

def hgrenadef(grenadelist):
    result = ''
    for i in range(4):
        if grenadelist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, 'T', str(grenadelist[i]), ' ', rgrenadedict[i]])
    return result

def hminingf(mininglist):
    result = ''
    for i in range(4):
        if mininglist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, 'T', str(mininglist[i]), ' ', rminingdict[i]])
    return result

def haccf(acclist):
    result = ''
    for i in range(3):
        if acclist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, raccessorydict[i]])
    return result

def hsuitf(suitlist):
    result = ''
    for i in range(4):
        if suitlist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, 'T', str(suitlist[i]), ' ', rsuitdict[i]])
    return result

def hmiscf(misclist):
    result = ''
    for i in range(6):
        if misclist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, rmiscdict[i]])
    return result

def hstructuref(structlist):
    result = ''
    for i in range(3):
        if structlist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, rstructuredict[i], ' '])
    return result

def hstructmodf(structlist):
    result = ''
    for i in range(3):
        for j in range(1, 4):
            if structlist[i][j]:
                if len(result) > 0:
                    result = result + ', '
                result = ''.join([result, rstructuremodlist[i][j]])
    return result

def halphakillf(akilllist):
    result = ''
    for i in range(6):
        if akilllist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, str(akilllist[i]), ' ', ralphakillsdict[i]])
    return result

def hzstructkillf(zkilllist):
    result = ''
    for i in range(5):
        if zkilllist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, str(zkilllist[i]), ' ', rzstructurekillsdict[i]])
    return result

def zombieinfocondense(zplayer, txtpath, f):
    # df = pd.DataFrame(columns=['Player Name', 'Handle', 'Result', 'Major Rooms Captured', 'Starting Alpha',
    #                                'Alphas Built', 'Strains Purchased', 'Upgrades Purchased', 'Advanced Infestations',
    #                                'Ultimate Infestation', 'Hangars Captured', 'Structures Built',
    #                                'Infestation Level Timings', 'Greater Nydus Timings',
    #                                'Marine Captures', 'Cocoons Made', 'Drop Pods Used', 'Structures Built', 'Siphons'])
    data = {}
    ztab = PrettyTable()
    ztab.field_names = ['Player Name', 'Handle', 'Result', 'Major Rooms Captured', 'Starting Alpha',
                                   'Alphas Built', 'Strains Purchased', 'Upgrades Purchased', 'Advanced Infestations',
                                   'Ultimate Infestation', 'Hangars Captured', 'Structures Built',
                                   'Infestation Level Timings', 'Greater Nydus Timings',
                                   'Marine Captures', 'Cocoons Made', 'Drop Pods Used', 'Structures Built #', 'Siphons']

    data['Player Name'] = zplayer.playername
    data['Handle'] = zplayer.handle
    data['Result'] = bool_to_victory(zplayer.victory)
    data['Major Rooms Captured'] = zmajorroomf(zplayer.majorroomcaptures)
    data['Starting Alpha'] = zplayer.startingalpha
    data['Alphas Built'] = zalphasbuiltf(zplayer.alphasbuilt)
    data['Strains Purchased'] = zstrainf(zplayer.strainpurchases)
    data['Upgrades Purchased'] = zupgradef(zplayer.upgradepurchases)
    data['Advanced Infestation'] = zadvinff(zplayer.advancedinfestations)
    data['Ultimate Infestation'] = zplayer.ultimateinfestation
    data['Hangars Captured'] = zhangarsf(zplayer.hangarcaptures)
    data['Structures Built'] = zstructf(zplayer.structurebuiltlist)
    data['Infestation Level Timings'] = zinftimingf(zplayer.infestationleveltimes)
    data['Greater Nydus Timings'] = zgreatertimingf(zplayer.greaternydustimings)
    data['Marine Captures'] = zplayer.marinecaptures
    data['Cocoons Made'] = zplayer.cocoonsmade
    data['Drop Pods Used'] = zplayer.droppodsused
    data['Structures Built #'] = zplayer.structurebuilt
    data['Siphons'] = zplayer.siphons

    # df = pd.concat([df, pd.DataFrame(data, index=[0])])
    ztab.add_row(list(data.values()))

    ztab.align = "l"
    ztabstring = ztab.get_string()
    print(ztabstring, file=f)

def zmajorroomf(mrlist):
    result = ''
    for i in range(5):
        if mrlist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, rmajorroomdict[i]])
    return result

def zalphasbuiltf(alist):
    result = ''
    alist_copy = alist.copy()
    for alpha in alist_copy:
        alpha[0] -= alpha[1]
    for i in range(5):
        if alist_copy[i][0]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, rt2alphasdict[i], ': ', str(alist_copy[i][0])])
        elif alist_copy[i][1]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, rt2alphasdict[i], ': ', str(alist_copy[i][1])])
    return result

def zstrainf(slist):
    result = ''
    slist_copy = slist.copy()
    for strain in slist_copy:
        strain[0] -= strain[1]
        strain[1] -= strain[2]
    for i in range(4):
        temp = ''
        if any(slist_copy[i]):
            if len(result) > 0:
                result = result + '/ '
            for j in range(3):
                if len(temp) > 0:
                    temp = temp + ', '
                if slist_copy[i][j]:
                    result = ''.join([result, 'T', str(j+1), ' ', rstrainsdict[i], ': ', str(slist_copy[i][j])])
        if len(temp) > 0:
            result = ''.join([result, temp])
    return result

def zupgradef(ulist):
    result = ''
    for i in range(5):
        if ulist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, rzupgradesdict[i]])
            if i == 4:
                result = ''.join([result, '(', str(ulist[4]), ')'])
    return result

def zadvinff(alist):
    result = ''
    for i in range(5):
        if alist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, rzadvupgradesdict[i]])
    return result

def zhangarsf(hlist):
    result = ''
    for i in range(3):
        if hlist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, rhangardict[i]])
    return result

def zstructf(slist):
    result = ''
    for i in range(5):
        if slist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, rzupgradesdict[i], ': ', str(slist[i])])
    return result

def zinftimingf(tlist):
    result = ''
    for i in range(5):
        if tlist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, str(datetime.timedelta(seconds=tlist[i]))])
    return result

def zgreatertimingf(glist):
    result = ''
    for i in range(len(glist)):
        if glist[i]:
            if len(result) > 0:
                result = result + ', '
            result = ''.join([result, str(datetime.timedelta(seconds=glist[i]))])
    return result
