import requests

# Set your Snyk API token, organization ID, and project and issue IDs
TOKEN = input("your-api-token: ")
ORG_ID = input("your-orgID: ")
PROJECT_ID = input("your-projectID: ")
ISSUE_ID = input("your-issueID: ")

# Set ignore URL
ignore_url = f"https://api.snyk.io/api/v1/org/{ORG_ID}/project/{PROJECT_ID}/ignore/{ISSUE_ID}"

# Make the POST request to ignore the issue
ignore_response = requests.post(ignore_url, headers={
    "Content-Type": "application/json",
    "Authorization": f"token {TOKEN}"
}, json={
    "reason": "I do not like it",
    "reasonType": "not-vulnerable",
    "disregardIfFixable": False
})

# Check the status code of the response
if ignore_response.status_code != 200:
    print(f"Error ignoring issue: {ignore_response.text}")
else:
    print("Issue ignored successfully")