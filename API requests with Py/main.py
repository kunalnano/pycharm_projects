import requests
import json

usr_name = input("Your name: ")
usr_token = input("Your token: ")
usr_url = input("Enter your URL: ")

# GitLab URL - https://gitlab.com/api/v4//users?username=:username

usr_headers = {'User-Agent': f'{usr_name} ({usr_token})'}

response = requests.get(usr_url, headers=usr_headers)
print(f'{response.status_code} - {response.reason}')

if response.status_code >= 300:
    exit()

my_projects = response.json()

print(my_projects)

for project in my_projects:
    print(f"Project Created: {project['created_at']}\n Project ID: {project['id']}\n Project Name: {project['name']}\n Project URL: {project['web_url']}\n")

response_commits = requests.get("https://gitlab.com/api/v4//projects/36897390/repository/commits").text

print(response_commits)

filename = input("Enter your filename in .json: ")

with open(filename, 'w', encoding="utf-8") as file:
    file.write(response_commits)
