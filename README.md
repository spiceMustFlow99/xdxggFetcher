# xdx.gg LoL Rank Fetcher

A simple Python script that fetches ranked information (SoloQ & Flex) from xdx.gg (EUW).

There is a fetch request named `summonerName-region` (e.g. `thebausffs-euw`) that contains information about:
- the player's rank
- total wins and losses
- a list of matches with their corresponding match IDs

Each match ID can be used to perform another fetch request with the same name, which provides detailed match data such as:
- whether the player won or lost
- participating players
- additional match statistics


## Example

THEBAUSFFS  
======== SOLOQ ========  
DIAMOND III - 61 LP  
Wins: 13 | Losses: 15  
Winrate: 46.43%  
======== FLEXQ ========  
UNRANKED  
===== LAST 20 GAMES =====  
Wins: 8 | Losses: 12  
Winrate: 40.0%

## Installation

pip install -r requirements.txt

## Run

python xdxggFetcher.py
