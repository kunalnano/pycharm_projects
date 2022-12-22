import requests

TOKEN = "ffc32183-089f-4820-b009-02f845103670"
ORG_ID = "47f8d945-2af9-4b09-b8d9-6afe4f6e288a"

issues = []

# Retrieve a list of projects within the organization
projects_url = f"https://api.snyk.io/rest/orgs/{ORG_ID}/projects?version=2022-04-06~experimental"
projects_response = requests.get(projects_url, headers={
    "Content-Type": "application/json",
    "Authorization": f"token {TOKEN}"
})
projects_data = projects_response.json()
project_ids = [p["id"] for p in projects_data["data"]]

# Retrieve a list of issues for each project
for project_id in project_ids:
    issues_url = f"https://api.snyk.io/rest/orgs/{ORG_ID}/issues?&project_id={project_id}&version=2022-04-06~experimental"
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

# Ignore all of the issues
for issue in issues:
    ignore_url = f"https://snyk.io/api/v1/org/{ORG_ID}/project/{issue['projectID']}/ignore/{issue['issueID']}"
    ignore_response = requests.post(ignore_url, headers={
        "Content-Type": "application/json",
        "Authorization": f"token {TOKEN}"
    }, json={
        "reason": "I do not like it",
        "reasonType": "not-vulnerable",
        "disregardIfFixable": False
    })
    print(f"Issue {issue['issueID']} on project {issue['projectID']} ignored")