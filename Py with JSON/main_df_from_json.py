import json
import pandas as pd
from tabulate import tabulate
from flatten_json import flatten


json_api_output = "/Users/alsharma/Documents/Indeed/retest issue/projects_devops_org.json"

with open(json_api_output, 'r') as j:
    contents = json.loads(j.read())

d = json.dumps(contents)

"""
# Flatten data for License Info
df_license = pd.json_normalize(contents, record_path=['results', 'id'])

# Create Columns
df_license.columns = df_license.columns.map(lambda x: x.split(".")[-1])
print(tabulate(df_license, headers='keys', tablefmt='psql'))

"""
# Flatten data for Project Info
df_projects = pd.json_normalize(contents, record_path=['results', 'projects'])

# Create Columns
df_projects.columns = df_projects.columns.map(lambda x: x.split(".")[-1])
print(tabulate(df_projects, headers='keys', tablefmt='psql'))

# Flatten data for Dependencies
df_deps = pd.json_normalize(contents, record_path=['results', 'dependencies'])
df_flattened = (flatten(record, '.') for record in df_deps)
pd.options.display.width = None

# Create Columns
df_deps.columns = df_deps.columns.map(lambda x: x.split(".")[-1])
print(tabulate(df_deps, headers='keys', tablefmt='psql'))

