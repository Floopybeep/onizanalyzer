import datetime
from playerclasses import *


def humanUCEcheck(event, name, humandict, humanset, zombieplayer):                         # checks for human events
    if name in structurecountset:
        humandict[event.pid].add_structurecounter(name)
    elif name in miningdict:
        humandict[event.pid].add_mining(name)
    elif name in structuredict:
        humandict[event.pid].add_structure(name)
    elif name in miscset:
        humandict[event.pid].add_misc(name)
    elif name in suitdict:
        humandict[event.pid].add_suit(name)
    elif name in weapondict:
        humandict[event.pid].add_weapon(weapon=name)
        if name in {'AresUnlocked', 'SpecOpsAresUnlocked', 'ArcWelderUnlocked', 'SpecOpsArcWelder'}:
            humandict[event.pid].add_experimental(name)
    elif name in weaponmoddict:
        humandict[event.pid].add_weapon(mod=name)
    elif name in aresmoddict:
        humandict[event.pid].add_aresmod(name)
        humandict[event.pid].weapons[6][1] = True
    elif name in grenadedict:
        humandict[event.pid].add_grenade(name)
    elif name in accessoryset:
        humandict[event.pid].add_accessories(name)
    elif name in experimentaldict:
        humandict[event.pid].add_experimental(name)
    elif name == 'DropshipsFueled' and event.pid in humanset:
        humandict[event.pid].dropshipfueledtime = datetime.timedelta(seconds=event.second)
    elif name == 'EmergencyCloakOn':
        humandict[event.pid].captures += 1
        zombieplayer.marinecaptures += 1


def zombieUCEcheck(event, name, zombieplayer, z_id):
    if event.player != None and event.player.pid == z_id:
        if name in strainsdict and event.count == 0:
            zombieplayer.strain_purchase(name)
        elif name in majorroomdict:
            zombieplayer.majorroom_capture(name)
        elif name in zupgradesdict and event.count == 0:
            zombieplayer.upgrade_purchase(name)
        elif name in zadvancedinfestationsdict:
            zombieplayer.advancedinfestation_purchase(name)
            if name == 'SiphonFuel' and event.count == 0:
                zombieplayer.siphons += 1
        elif name in infestationleveldict:
            zombieplayer.infestationlevel_time(name, event.second)
        elif name in ultimateinfestationdict:
            zombieplayer.ultimateinfestation_chosen(name)

