## How to install
Create new project, then:
1. `git clone --branch master https://github.com/Jacob1507/script.git`
2. `cd script`
3. `pip install --editable .`
4. `pip install requirements.txt`

## Using commands
Usage: script [ command ] [ options ]

All possible commands:\
 `group_teams` `players-highest-stats` `players` `teams-stats`
 
To view possible options use:\
 `script [ command ] --help`


*please note that commands request API from external source and it might take some time to process all data
## Examples
### players

````
C:\project\script> script players --help

Usage: script players [OPTIONS]

Options:
  --name TEXT  Search players by name
  --help       Show this message and exit.

````

````
C:\project\script> script players --name michael


Michael Smith - Boston Celtics (BOS)
Michael Ansley - Orlando Magic (ORL)
Michael Adams - Denver Nuggets (DEN)
Michael Curry - Philadelphia 76ers (PHI)
<rest of players>
````

### teams-stats

````
C:\project\script> script teams-stats --season 2021
Atlanta Hawks
        won games as home team: 19
        won games as visitor team: 14
        lost games as home team: 24
        lost games as visitor team: 31


    Boston Celtics
        won games as home team: 26
        won games as visitor team: 18
        lost games as home team: 19
        lost games as visitor team: 25
<rest of teams>
````

Parameters:

* `--output`:
    * `json`  - save data in json format
    
Commands `group-teams` and `players-highest-stats` don't require additional parameters.
