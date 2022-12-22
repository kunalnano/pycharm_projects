import json
import pandas as pd
import tabulate

json_file = "/Users/alsharma/Documents/GitHub/Indeed/package.json"

with open(json_file, 'r') as j:
     json_file_contents = json.loads(j.read())

# print(json.dumps(contents, indent= 6))

df = pd.read_json(json_file)

# Flatten data
df_nested_list = pd.json_normalize(json_file_contents, record_path=['artifacts'])

# pd.options.display.width = None
# print(tabulate(df_nested_list, headers='keys', tablefmt='pretty'))
# print(df_nested_list)
print(df_nested_list.to_markdown(tablefmt="grid"))


