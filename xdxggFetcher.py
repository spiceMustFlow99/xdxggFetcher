import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def printRank(queueName, tier, division, lp, wins, losses):
    print(f"========= {queueName} =========")
    if not tier or wins + losses == 0:
        print("UNRANKED")
        return
    winrate = round((wins / (wins + losses)) * 100, 2)
    print(f"{tier} {division} - {lp} LP")
    print(f"Wins: {wins} | Losses: {losses}")
    print(f"Winrate: {winrate}%")


def safeInt(value):
    if value is None or value == "":
        return 0
    return int(value)


def getRecentWinrate(player_name, region="euw", amount=20):
    baseUrl = f"https://p1.xdx.gg/rid/1/{player_name.lower()}-{region}"
    response = requests.get(baseUrl, headers=HEADERS)
    if response.status_code != 200:
        print("Error while loading match history.")
        return
    data = response.json()
    matches = data.get("matches", [])
    if not matches:
        print("No matches found.")
        return
    recentMatches = matches[:amount]
    wins = 0
    losses = 0
    for match in recentMatches:
        matchId = match[0]
        matchUrl = f"https://pp1.xdx.gg/match/1/euw/{matchId}"
        matchResponse = requests.get(matchUrl, headers=HEADERS)
        if matchResponse.status_code != 200:
            continue
        matchData = matchResponse.json()
        names = matchData.get("riotIdGameName", [])
        winners = matchData.get("winner", [])
        normalizedNames = [
            name.split("#")[0].split("-")[0].lower()
            for name in names
        ]
        normalizedPlayer = playerName.lower()
        if normalizedPlayer not in normalizedNames:
            continue
        index = normalizedNames.index(normalizedPlayer)
        if winners[index] == 1:
            wins += 1
        else:
            losses += 1
    total = wins + losses
    print(f"===== LAST {amount} GAMES =====")
    if total == 0:
        print("No usable matches.")
        return
    winrate = round((wins / total) * 100, 2)
    print(f"Wins: {wins} | Losses: {losses}")
    print(f"Winrate: {winrate}%")


def getPlayerData(name, region="euw"):
    url = f"https://p1.xdx.gg/rid/1/{name.lower()}-{region}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print("Request Error:", response.status_code)
        return
    try:
        data = response.json()
    except:
        print("Invalid data recived.")
        return
    # SOLOQ
    soloWins = safeInt(data.get("solo-wins"))
    soloLosses = safeInt(data.get("solo-losses"))
    soloTier = data.get("solo-tier", "")
    soloDiv = data.get("solo-division", "")
    soloLp = safeInt(data.get("solo-lp"))
    # FLEXQ
    flexWins = safeInt(data.get("flex-wins"))
    flexLosses = safeInt(data.get("flex-losses"))
    flexTier = data.get("flex-tier", "")
    flexDiv = data.get("flex-division", "")
    flexLp = safeInt(data.get("flex-lp"))
    print("\n"+name.upper())
    printRank("SOLOQ", soloTier, soloDiv, soloLp, soloWins, soloLosses)
    printRank("FLEXQ", flexTier, flexDiv, flexLp, flexWins, flexLosses)
    getRecentWinrate(name)
    print()


playerName = input("Enter Name (without #EUW): ")
getPlayerData(playerName)