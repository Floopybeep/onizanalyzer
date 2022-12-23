from humanupgradecomplete import *

tempset = {'UpgradeCompleteEvent', 'UnitTypeChangeEvent', 'UnitBornEvent', 'UnitInitEvent', 'PlayerStatsEvent'}


def winloss_to_victory(result):
    if result == 'Win':
        return True
    elif result == 'Loss':
        return False
    else:
        return None


def extract_playerinfo(replay):                                         # input: replay / output: list of h/z objects
    humandict, zombieplayer = {}, None

    for human in replay.humans:
        if human.pid > 8: pass

        victory = winloss_to_victory(human.result)

        if human.play_race == 'Terran':
            humandict[human.pid] = marineinfo(name=human.name, pid=human.pid, handle=human.toon_handle, role='Human', victory=victory)
        elif human.play_race == 'Zerg':
            zombieplayer = zombieinfo(name=human.name, pid=human.pid, handle=human.toon_handle, role='Zombie', victory=victory)
            z_player_hangar_kill_check(human.killed_units, zombieplayer)

    if victory is None:
        for human in replay.humans:
            if human.pid > 8: pass
            if human.play_race == 'Terran':
                for unit in human.units:
                    if dropship_player_check(unit):
                        humandict[human.pid].victory = True
                        zombieplayer.victory = False
                if humandict[human.pid].victory is None:
                    humandict[human.pid].victory = False
        if zombieplayer.victory is None:
            zombieplayer.victory = True

    return humandict, zombieplayer


def dropship_player_check(unit):
    if 188 <= unit.location[0] <= 211 and 212 <= unit.location[1] <= 255:
        return 1
    elif 212 <= unit.location[0] <= 235 and 212 <= unit.location[1] <= 255:
        return 2
    elif 236 <= unit.location[0] <= 256 and 212 <= unit.location[1] <= 255:
        return 3
    else:
        return 0


def z_player_hangar_kill_check(units, zombieplayer):
    for unit in units:
        # Alpha, Beta, Delta hangar
        if unit.location == (30, 55):
            zombieplayer.hangarcaptures[0] = True
        elif unit.location == (150, 225):
            zombieplayer.hangarcaptures[1] = True
        elif unit.location == (204, 40):
            zombieplayer.hangarcaptures[2] = True


def extract_eventinfo(replay, humandict, zombieplayer):
    humanlist = []
    for key in humandict:
        humanlist.append(humandict[key].pid)
    humanset = set(humanlist)
    z_id = zombieplayer.pid

    for event in replay.events:
        if event.name in tempset:
            if event.name == 'UpgradeCompleteEvent':
                UpgradeCompleteEventCheck(event, humandict, humanset, zombieplayer)
            elif event.name == 'UnitTypeChangeEvent':
                UnitTypeChangeEventCheck(event, zombieplayer)
            elif event.name == 'UnitBornEvent':
                UnitBornEventCheck(event, zombieplayer)
            elif event.name == 'UnitInitEvent':
                UnitInitEventCheck(event, humandict, zombieplayer)
            elif event.name == 'PlayerStatsEvent':
                PlayerStatsEventCheck(event, zombieplayer, z_id)



    # extract the following information
    # 1. roomcaptures
    # 4. totalgasincome
    # 5. totalgasspent


def UpgradeCompleteEventCheck(event, humandict, humanset, zombieplayer):
    name = event.upgrade_type_name
    z_id = zombieplayer.pid
    humanUCEcheck(event, name, humandict, humanset, zombieplayer)
    zombieUCEcheck(event, name, zombieplayer, z_id)


def UnitTypeChangeEventCheck(event, zombieplayer):
    name = event.unit_type_name

    if name == 'MassiveCocoon':
        zombieplayer.cocoonsmade += 1
        zombieplayer.cocoonids.add(event.unit_id_index)
    elif name in t2alphadict and event.unit_id_index in zombieplayer.cocoonids:
        zombieplayer.t2alpha_create(name)
        zombieplayer.cocoonids.discard(event.unit_id_index)


def UnitBornEventCheck(event, zombieplayer):
    name = event.unit_type_name

    if name == 'ZergDropPod':
        zombieplayer.droppodsused += 1
    elif name == 'MassiveCocoon':
        zombieplayer.cocoonsmade += 1
    elif name in t1alphadict:
        zombieplayer.t1alpha_create(name)
        if zombieplayer.startingalpha is None:
            zombieplayer.startingalpha = t1alphatonamedict[name]


def UnitInitEventCheck(event, humandict, zombieplayer):
    name = event.unit_type_name

    if name == 'ExplorationDroid':
        humandict[event.control_pid].explorationdroidsmade += 1
    elif name in zstructuredict:
        zombieplayer.structure_create(name)
        zombieplayer.structurebuilt += 1
    elif name == 'GreaterNydusWorm':
        zombieplayer.greaternydustimings.append(event.second)


def PlayerStatsEventCheck(event, zombieplayer, z_id):
    if event.pid == z_id:
        zombieplayer.totalgasspent = event.resources_used_current
        zombieplayer.totalgasincome = event.resources_used_current + event.vespene_current
