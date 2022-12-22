from snyk.client import SnykClient

# To get this value, get it from a Snyk organizations settings page
snyk_org = "47f8d945-2af9-4b09-b8d9-6afe4f6e288a"
snyk_user = "a3069cf0-40b2-4f32-8554-47072a897af3"
snyk_token = "ffc32183-089f-4820-b009-02f845103670"

# to use the rest endpoint you MUST include a version value and the url of the v3 api endpoint as shown below
rest_client = SnykClient(snyk_token, version="2022-02-16~experimental", url="https://api.snyk.io/rest")
print(rest_client.get(f"/orgs/{snyk_org}").json())

# this supports overriding rest versions for a specific GET requests:
user = rest_client.get(f"orgs/{snyk_org}/users/{snyk_user}", version="2022-02-01~experimental").json()
print(user)

# pass parameters such as how many results per page
params = {"limit": 10}

targets = rest_client.get(f"orgs/{snyk_org}/targets", params=params)
print(targets)
