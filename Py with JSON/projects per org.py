import pandas as pd
import requests

org_url = 'https://snyk.io/api/v1/org/orgID/licenses?sortBy=license&order=asc'
headers = {
    'orgID': '24005d15-97d3-46c3-89ed-e52caffa93e0',
    'Authorization': '43f364f7-8167-4ce0-96db-df0205d1a765',
}

response = requests.get(org_url, headers=headers).json()

print(response).split('{')

# data_df = pd.read_json(response)
norm_df = pd.json_normalize(response)
print(norm_df.head())


