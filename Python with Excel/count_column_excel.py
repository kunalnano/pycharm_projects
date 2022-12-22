import pandas as pd
import numpy as np
import openpyxl
from urllib.parse import urlparse
from tabulate import tabulate

# Read the Excel into Pandas DF
df_issues = pd.read_csv("/Users/alsharma/Downloads/c6b6599e-f3c5-4062-a733-8cb9a8f4b416.csv")

df_issues.head()

most_affected = df_issues["RESOLVED_CURRENT"].value_counts()
org_list = np.expand_dims(most_affected, axis=0)
# count_of_orgs = len(pd.unique(df_issues['org_name']))

count_of_orgs = df_issues['RESOLVED_CURRENT'].nunique()

print(count_of_orgs)
# print(tabulate(org_list, headers='keys', tablefmt='fancy_grid'))
print(df_issues["ORG_NAME"], most_affected.to_markdown(tablefmt='psql'))


# with pd.ExcelWriter('/Users/alsharma/Downloads/c6b6599e-f3c5-4062-a733-8cb9a8f4b416.csv', engine='openpyxl', mode='a') as writer:
#    most_affected.to_excel(writer, sheet_name='Most Affected Orgs')