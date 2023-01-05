import os

path = os.path.expanduser('~/documents/ONIZanalyzersettings.txt')

with open(path, 'r') as f:
    print(f.readline())
    print(f.readline())

