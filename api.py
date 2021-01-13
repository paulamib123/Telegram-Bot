import requests

def getInsult():
    parameters = {
        "Language": "en",
        "Format": "json"
    }
    response = requests.get("https://insult.mattbas.org/api/insult.json", params=parameters)
    insult = response.json()["insult"]
    return insult

def getInsultWithName(name):
    parameters = {
        "Language" : "en",
        "Format" : "json",
        "who" : name
    }
    response = requests.get("https://insult.mattbas.org/api/insult.json", params=parameters)
    insult = response.json()["insult"]
    return insult

def getCompliment():
    response = requests.get("https://complimentr.com/api")
    compliment = response.json()["compliment"]
    return compliment


getInsult()
getInsultWithName("Elle")
getCompliment()
