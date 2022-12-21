import sc2reader
from playerclasses import *


def humanUCEcheck(event, name, humandict):
    if name in weapondict:
        humandict[event.pid].add_weapon(weapon=name)
    elif name in weaponmoddict:
        humandict[event.pid].add_weapon(mod=name)
    elif name in grenadedict:
        humandict[event.pid].add_grenade(name)
    elif name in miningdict:
        humandict[event.pid].add_mining(name)
    elif name in accessoryset:
        humandict[event.pid].add_accessories(name)
    elif name in suitdict:
        humandict[event.pid].add_suit(name)
    elif name in structuredict:
        humandict[event.pid].add_structure(name)
    elif name in miscset:
        humandict[event.pid].add_misc(name)
    elif name in experimentaldict:
        humandict[event.pid].add_experimental(name)

