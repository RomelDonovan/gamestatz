from tabulate import tabulate
import requests
import json

# Fetch henrikdev.xyz api data
def retrieve_data(username, tag):
    resp = requests.get(f"https://api.henrikdev.xyz/valorant/v2/mmr/na/{username}/{tag}")
    data = json.loads(resp.text)
    return data

# Filter data 
def parse_data(user_data):
    username = user_data["data"]["name"]
    tag = user_data["data"]["tag"]
    rank = user_data["data"]["current_data"]["currenttierpatched"]
    tier = user_data["data"]["current_data"]["ranking_in_tier"]
    return {"username": username, "tag": tag, "rank": rank, "RR": tier}

# Create table and return to user
def display_data(stats):
    rows = []
    headers = ["GameStatz", ""]
    for k, v in stats.items():
        rows.append([k.title(), v])
    print(f'\n{tabulate(rows, headers=headers)}')

def main():
    try:
        username = input("\nPlease enter your Valorant username:\n")
        tag = input("\nPlease enter your Valorant tag:\n")
        user_data = retrieve_data(username, tag)
        formatted_data = parse_data(user_data)
        display_data(formatted_data)
    except Exception as error:
        print("\nSorry, invalid username or tag. Please input a valid username and tag")

if __name__ == '__main__':
    main()