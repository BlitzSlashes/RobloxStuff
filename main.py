import requests
from termcolor import colored
import sys


def search(username: str, opt=''):
    try:
        req = requests.get(
            f"https://www.roblox.com/search/users/results/?keyword={username}/UserSearchResults")
        res = req.json()
        if res:
            if opt:
                ctx = dict(result=res['UserSearchResults'][0][opt])
                return ctx
            return res['UserSearchResults'][0]
    except TypeError:
        return f"There isn't any info about {colored(username, color='red')}"


def main():
    try:
        username = sys.argv[1].lower()
        option = sys.argv[2].lower()
        options = {
            'id': 'UserId',
            'name': 'Name',
            'about': 'Blurb',
            'old_names': 'PreviousUserNamesCsv',
            'status': 'IsOnline',
            'main_group': 'PrimaryGroup'
        }
        res = search(username, opt=options[option])
        return res
    except IndexError:
        return search(username)


print(main())
