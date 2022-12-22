import requests
from pprint import pprint

BASE_URL = 'https://api.github.com'
USERNAME = 'al5harma'
TOKEN = "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"
REPOSITORY = 'nodejs-goof'
ISSUE = 20

headers = {"Authorization": f"token{TOKEN}", "User-Agent": "al5harma", "Accept": "application/vnd.github+json"}

URL = f'{BASE_URL}/repos/{USERNAME}/{REPOSITORY}/assignees'

# response = requests.get(URL, auth=(USERNAME, TOKEN))

response = requests.get(URL, headers=headers)

print(f"{response.status_code} - {response.reason}")

if response.status_code >= 300:
    exit()

data = response.json()

# reactions = data['reactions']

pprint(data)
# pprint(reactions)



