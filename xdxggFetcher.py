import requests

def printRank(queueName, tier, division, lp, wins, losses):
    if not tier or wins + losses == 0:
        print(f"===== {queueName} =====")
        print("UNRANKED")
        return
    winrate = round((wins / (wins + losses)) * 100, 2)
    print(f"===== {queueName} =====")
    print(f"{tier} {division} - {lp} LP")
    print(f"Wins: {wins} | Losses: {losses}")
    print(f"Winrate: {winrate}%")


def safeInt(value):
    if value is None or value == "":
        return 0
    return int(value)


def getPlayerData(name, region="euw"):
    url = f"https://p1.xdx.gg/rid/1/{name.lower()}-{region}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

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
    printRank("FLEX", flexTier, flexDiv, flexLp, flexWins, flexLosses)
    print()


playerName = input("Enter Name (without #EUW): ")
getPlayerData(playerName)