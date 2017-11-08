import fut
import json
import os
import configparser
from fut.model import dbConnector as DB

def getCredentials():
    """    Lädt die Zugangsdaten für die Datenbank + EA.

    :rtype: Dictionary
    :return credentials: Zugangsdaten EA + DB
    """
    config  = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../model', 'mycredentials.conf'))

    credentials = {
        "DB_Host" : config.get("configuration-DB", "host"),
        "DB_User" : config.get("configuration-DB", "user"),
        "DB_Pass" : config.get("configuration-DB", "pass"),
        "DB_Name" : config.get("configuration-DB", "db"),
        "EA_Mail" : config.get("configuration-EA", "mail"),
        "EA_Pass" : config.get("configuration-EA", "pass"),
        "EA_Secr" : config.get("configuration-EA", "secret")
    }

    return credentials

credentials = getCredentials()

#FUT-Objekt
#Verbindung zu EA
fut = fut.Core(
    credentials['EA_Mail'],
    credentials['EA_Pass'],
    credentials['EA_Secr'],
    debug=True
)


def getPlayerViaNameFromTransfermarket(name, fut):
    matchedPlayer = None
    players = fut.players
    if name in players:
        matchedPlayer = players[name]

    return matchedPlayer

    #Test Query
q = "SELECT * FROM Player"

#Suche
items = fut.searchAuctions(ctype='player', level='gold')

#JSON Dump
dump = json.dumps(items)

#Verbindung zur DB
db = DB.Database(
    credentials['DB_Host'],
    credentials['DB_User'],
    credentials['DB_Pass'],
    credentials['DB_Name']
)

#getPlayerViaNameFromTransfermarket('Garcia', fut)


#q = "SHOW DATABASES"
#q = "SHOW TABLES"

#result = db.insert(q)
#result = db.query(q)
#print(result)

#parsed = json.loads(items)
#print(json.dumps(parsed, indent=4, sort_keys=True))
#print(items)


#nations = fut.nations()

#leagues = fut.leagues()
#teams = fut.teams()
#stadiums = fut.stadiums()
#players = fut.players()
#playestyles = fut.playstyles()
fut.logout()
print('Done')