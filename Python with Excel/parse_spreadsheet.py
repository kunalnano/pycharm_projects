# reference URL - http://pytolearn.csd.auth.gr/b4-pandas/40/moddfcols.html
import pandas as pd
import openpyxl
from urllib.parse import urlparse
from tabulate import tabulate

# Read the Excel into Pandas DF
df_issues = pd.read_excel("/Users/alsharma/Documents/GitHub/Indeed/SAST_UID/11_9_to_11_16.xlsx")

"""
df_project_url = pd.read_excel("Reporting Beta_Hardcoded Secrets_110822.xlsx", sheet_name="CWE 547", usecols=["ISSUE_URL"])
df_project_url.columns = df_project_url.iloc[0]
project_url_df = df_project_url[1:]
"""

df_issues['Problem ID'] = df_issues['PROJECT_URL'].str.split('/').str[6]

# .str.split('#').str[0]

df_issues['Issue ID'] = df_issues['ISSUE_URL'].str.split('#').str[1].str.split('issue-').str[1]

# df_issues['Issue ID'] = df_issues['Issue ID'].str.split('issue-').str[1]

# df_issues['Org ID'] = df_issues['PROJECT_URL'].str.split('/').str[4]

print(tabulate(df_issues, headers='keys', tablefmt='fancy_grid', showindex=False))

df_issues.to_excel("Indeed SAST Projects rev 3.xlsx")



