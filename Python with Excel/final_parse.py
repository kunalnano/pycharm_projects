# reference URL - http://pytolearn.csd.auth.gr/b4-pandas/40/moddfcols.html
import pandas as pd
import openpyxl
from urllib.parse import urlparse
from tabulate import tabulate

# Read the Excel into Pandas DF
df_issues_fin = pd.read_excel("Indeed SAST Projects.xlsx")

df_issues_fin['Problem ID'] = df_issues_fin['ISSUE_URL'].str.split('#').str[0]

df_issues_fin['Problem ID'] = df_issues_fin['ISSUE_URL'].str.split('/').str[6]

df_issues_fin['Problem ID'] = df_issues_fin['ISSUE_URL'].str.split('/').str[6]

print(tabulate(df_issues_fin, headers='keys', tablefmt='fancy_grid', showindex=False))

df_issues_fin.to_excel("Indeed SAST Projects rev1.xlsx")

