import requests

URL = "https://remotive.com/api/remote-jobs"

def fetch_jobs(search_term=None):
    url = URL

    if search_term:
        url += f"?search={search_term}"

    response = requests.get(url)
    data = response.json()
    return data["jobs"]

def main(search):
    jobs = fetch_jobs(search)

    filtered_jobs = [job for job in jobs if "software" in job["title"].lower()]

    for job in filtered_jobs[:10]: #first 10 jobs
        print(job["company_name"], "-", job["title"])

if __name__ == "__main__":
    main(search="software")