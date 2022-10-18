# Valorant ask for username
from wsgiref import headers
from bs4 import BeautifulSoup
import requests
import json

# Use requests and beautiful soup 4 to web scrape tracker.gg
    # resp = requests.get("https://api.henrikdev.xyz/valorant/v1/account/"+username+'/'+tag)
    # data = json.loads(resp.text)
    # print("resp: ", resp.text)
    # print("json: ", json.loads(resp.text))
    # print("account level: ", data["data"]["account_level"])
def retrieve_data():
    # resp = requests.get("https://tracker.gg/valorant/profile/riot/"+ username +"%23" + tag + "/overview")
    # resp = requests.get("https://tracker.gg/valorant/profile/riot/Rude%23NA13/overview")
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }
    resp = requests.get("https://api.tracker.gg/api/v2/valorant/standard/matches/riot/fearflawless%23FEAR?type=competitive", headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    print(soup)



    

    # print(soup.prettify()) # print the parsed data of HTML


# win/lose, K/D, Headshot%, MMR
def parse_data():
    pass

# format data and return to user
def display_data():
    pass

def main():
    # username = input("Please enter your Valorant username:\n")
    # tag = input("Please enter your Valorant tag:\n")
    retrieve_data()
    parse_data()
    display_data()

if __name__ == '__main__':
    main()