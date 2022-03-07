## How to install
Create new project, then:
1. `git clone --branch master https://github.com/Jacob1507/script.git`
2. `cd script`
3. `pip install --editable .`
4. `pip install requirements.txt`

## Using commands
Usage: `script [ command ] [ options ]`

All possible commands:\
 `group-teams` `players-stats` `teams-stats`
 
To view possible options use:\
 `script [ command ] --help`


*please note that commands request API from external source and it might take some time to process all data
## Examples
### team-stats
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
### group-teams
```
C:\project\script> script group-teams

Southeast
        Atlanta Hawks
        Charlotte Hornets
        Miami Heat
        Orlando Magic
        Washington Wizards
Atlantic
        Boston Celtics
        Brooklyn Nets
        New York Knicks
        Philadelphia 76ers
        Toronto Raptors
<rest of groups>
```
### players-stats
```
C:\project\script> script players-stats --name james

Tallest player: James Johnson 2.03 meters
Heaviest player: LeBron James 113.4 kg
```

Parameters:

* `--name <player name>`
