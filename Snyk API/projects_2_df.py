import requests
import pandas as pd
from tabulate import tabulate


def normalize_json(json_data):
    normalized_data = []
    for issue in json_data["data"]:
        try:
            project_id = issue["projectId"]
        except KeyError:
            project_id = "N/A"  # default value if "projectId" is not present
        try:
            description = issue["description"]
        except KeyError:
            description = "N/A"  # default value if "description" is not present
        try:
            severity = issue["severity"]
        except KeyError:
            severity = "N/A"  # default value if "severity" is not present
        try:
            package = issue["package"]["name"]
        except KeyError:
            package = "N/A"  # default value if "package" is not present
        normalized_data.append({
            "projectID": project_id,
            "issueID": issue["id"],
            "description": description,
            "severity": severity,
            "package": package,
        })
    return normalized_data


TOKEN = "ffc32183-089f-4820-b009-02f845103670"
ORG_ID = "47f8d945-2af9-4b09-b8d9-6afe4f6e288a"
PROJECT_ID = "edf2a159-f8d4-4a88-8bc5-4172a8d93946"


def main():
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
    issues = []
    for project_id in project_ids:
        if PROJECT_ID and PROJECT_ID != project_id:
            continue  # skip this project if it doesn't match the filter
        issues_url = f"https://api.snyk.io/rest/orgs/{ORG_ID}/issues?&project_id={project_id}&version=2022-04-06~experimental"

        issues_response = requests.get(issues_url, headers={
            "Content-Type": "application/json",
            "Authorization": f"token {TOKEN}"
        })
        if issues_response.status_code != 200:
            print(f"Error retrieving list of issues for project {project_id}: {issues_response.text}")
            continue

        issues_data = issues_response.json()
        normalized_data = normalize_json(issues_data)

        issues.extend(normalized_data)

    # Convert the list of issues to a Pandas DataFrame
    df = pd.DataFrame(issues)

    # Print the DataFrame as a table
    print(tabulate(df, headers="keys", tablefmt="psql"))


if __name__ == "__main__":
    main()

