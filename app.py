# Valorant ask for username
import requests
import json

# Use requests and json to web scrape henrikdev

def retrieve_data(username, tag):
    resp = requests.get("https://api.henrikdev.xyz/valorant/v2/mmr/na/" + username + '/' + tag)
    data = json.loads(resp.text)
    print("Username: ", data["data"]["name"] + "#" + data["data"]["tag"])
    print("Rank: ", data["data"]["current_data"]["currenttierpatched"] + " RR: ", data["data"]["current_data"]["ranking_in_tier"])

# win/lose, MMR
def parse_data():
    pass

# format data and return to user
def display_data():
    pass

def main():
    username = input("Please enter your Valorant username:\n")
    tag = input("Please enter your Valorant tag:\n")
    retrieve_data(username, tag)
    parse_data()
    display_data()

if __name__ == '__main__':
    main()