import time

def log(text, logger_file):
    with open(logger_file, 'a') as f:
        f.write(text)
        f.close()

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
        f.write('Player Name\tRole\t\tRank\n')
        f.write('{0:15}\t{1:6}\t\t{2}\n'.format(zplayer.playername, zplayer.playerrole, zplayer.rank))
        for hplayer in humanlist:
            f.write('{0:15}\t{1:5}\t\t{2}\n'.format(hplayer.playername, hplayer.playerrole, hplayer.rank))
        f.write("\n\n")
        if zplayer.victory:
            f.write("Zombie victory\n")
        else:
            f.write("Human victory\n")
        f.close()

# def humaninfocondense(humandict):
#
# def zombieinfocondense(zplayer):
