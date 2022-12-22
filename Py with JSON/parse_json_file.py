import pandas as pd
import requests

response = pd.read_json('/Users/alsharma/Documents/Indeed/Users/response.json')

pd.json_normalize(response, record_path=['artifacts'])

print(response.to_markdown(tablefmt="grid"))

response.to_excel('Indeed Group Members.xlsx')

