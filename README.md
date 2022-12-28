# onizanalyzer

Things to do
 - Add ARES tank mods
 - Group processes into ONE PROCESS?
   - task manager shows 30 different processes lol
 - Add diverts
 - Add excel table of data
   - More complicated than I thought - how am I going to keep updating the dataframe?
 - Add save files to user/documents feature 
   - Maybe as onizanalyzer
 - Add duplicate checker
   - prototype is already made from arguing w frosky - I can reuse much of that
   - use bank signatures to match?


Much more down the line
- bank reclaimer
- .exe file size reduction (optimization)
  - Done by creating a fresh env and installing only the necessary packages
- discord bot


Needs Fixes
- human structures wonky? panda built 12 psis but shows only turrets and heal
- human structure count is wonky... panda built 94 turrets? no way
  - looks like turret upgrades count as turret builds, maybe change to UnitInitEvent?
- creep tower count is weird?
- cocoons made count is way too high? maybe insert playerid check? (count for marine?)


# Version Changes
- 1.0.0: Initial launch of beta version
- 1.0.1: Added initial barebones textfile output
- 1.0.2: Fleshed out textfile output to include full scope of the replay
- 1.0.3: bugfixes
- 1.0.4: (coming soon) Excel file output for user-custom data analysis