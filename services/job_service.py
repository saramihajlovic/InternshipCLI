import requests

URL = "https://remotive.com/api/remote-jobs"

def fetch_jobs(search_term=None):
    """Fetch jobs from the Remotive API, optionally filtering by a search term in the job title."""
    url = URL

    if search_term:
        url += f"?search={search_term}"

    response = requests.get(url)
    data = response.json()
    return data.get("jobs", [])