"""
Add a reaction to a GitHub issue

Issue: https://github.com/ariannedee/python-foundations-3-weeks/issues/1
API endpoint: https://docs.github.com/en/rest/reference/reactions#create-reaction-for-an-issue
Get access token: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal
-access-token#creating-a-token
"""
import requests

BASE_URL = 'https://api.github.com'
USERNAME = 'al5harma'
REPOSITORY = 'nodejs-goof'
TOKEN = "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"
ISSUE = 20
URL = f'{BASE_URL}/repos/{USERNAME}/{REPOSITORY}/issues/{ISSUE}/reactions'

valid_reactions = ['+1', '-1', 'laugh', 'confused', 'heart', 'hooray', 'rocket', 'eyes']

reaction = input(f"Enter one of these reactions: {valid_reactions}\nreaction: ")

if reaction not in valid_reactions:
    print(f"{reaction} is not a valid reaction")
    exit()

data = {'content': reaction}

response = requests.post(URL, json=data, auth=(USERNAME, TOKEN))

print(f"{response.status_code} - {response.reason}")
