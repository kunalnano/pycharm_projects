import requests

TOKEN = input("Enter your Snyk API token: ")
ORG_ID = input("Enter your Snyk organization ID: ")
PROJECT_ID = input("Enter the ProjectID to filter on (leave empty to retrieve all projects): ")

issues = []

# Retrieve a list of projects within the organization
projects_url = f"https://api.snyk.io/rest/orgs/{ORG_ID}/projects?version=2022-04-06~experimental"
projects_response = requests.get(projects_url, headers={
    "Content-Type": "application/json",
    "Authorization": f"token {TOKEN}"
})
if projects_response.status_code != 200:
    print(f"Error retrieving list of projects: {projects_response.text}")
    exit()

projects_data = projects_response.json()
try:
    project_ids = [p["id"] for p in projects_data["data"]]
except KeyError:
    print(f"Error: 'data' not found in response: {projects_data}")
    exit()

# Retrieve a list of issues for each project
for project_id in project_ids:
    if PROJECT_ID and PROJECT_ID != project_id:
        continue  # skip this project if it doesn't match the filter
    issues_url = f"https://api.snyk.io/rest/orgs/{ORG_ID}/issues?&project_id={PROJECT_ID}&version=2022-04-06~experimental"

    issues_response = requests.get(issues_url, headers={
        "Content-Type": "application/json",
        "Authorization": f"token {TOKEN}"
    })
    issues_data = issues_response.json()
    project_issues = [issue["id"] for issue in issues_data["data"]]
    for issue_id in project_issues:
        issues.append({"projectID": project_id, "issueID": issue_id})

# Retrieve a list of non-code issues within the organization
issues_url = "https://snyk.io/api/v1/reporting/issues/latest"
issues_response = requests.post(issues_url, headers={
    "Content-Type": "application/json",
    "Authorization": f"token {TOKEN}"
}, json={
    "filters": {
        "orgs": [ORG_ID],
        "severity": ["critical", "high"],
        "fixable": False
    }
})
issues_data = issues_response.json()
non_code_issues = [{"projectID": i["project"]["id"], "issueID": i["issue"]["id"]} for i in issues_data['results']]
issues.extend(non_code_issues)

# Ignore everything in a project
for issue in issues:
    ignore_url = f"https://snyk.io/api/v1/org/{ORG_ID}/project/{issue['projectID']}/ignore"
    ignore_response = requests.post(ignore_url, headers={
        "Content-Type": "application/json",
        "Authorization": f"token {TOKEN}"
    }, json={
        "reason": "I do not like it",
        "reasonType": "not-vulnerable",
        "disregardIfFixable": False
    })
    if ignore_response.status_code != 200:
        print(f"Error ignoring issues on project {issue['projectID']}: {ignore_response.text}")
    else:
        print(f"All issues on project {issue['projectID']} ignored")