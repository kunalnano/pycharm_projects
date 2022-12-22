import json
import pandas as pd
import requests

gh_url = 'https://api.github.com/repos/al5harma/nodejs-goof/assignees'
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer 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',
}

response = requests.get(gh_url, headers=headers).json()

print(response)

data_df = pd.read_json(response)
norm_df = pd.json_normalize(data_df)

data_df.head()


