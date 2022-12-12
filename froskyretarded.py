from os import listdir
from os.path import isfile, join

games = {}
count_valids = 0
count_dupes = 0

folderpath = "C:/Users/wooil/Downloads/Replays_All"
onlyfiles = [join(folderpath, f) for f in listdir(folderpath) if isfile(join(folderpath, f))]

for file in onlyfiles:
    with open(file, encoding="UTF-8") as f:
        lines = f.readlines()

        if 'Updated' in file:
            game_id = file[72:-5]
        else:
            game_id = file[68:-5]

        # Assigns "Date - P1 - P2 - P3 - P4 - P5" as key in dictionary
        tempstring = "{}".format(lines[5:26])
        # If no collision, assigns text file
        if tempstring not in games:
            games[tempstring] = game_id
            count_valids += 1
        else:
            print("Duplicate game detected, Duplicate file name:", game_id, " / Original file name:", games[tempstring])
            count_dupes += 1


print("total valid files: ", count_valids)
print("total duplicate files: ", count_dupes)
