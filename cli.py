import click

from services.job_service import fetch_jobs
from utils.filters import filter_by_category

@click.command()
@click.option("--search", default="", help="Search keyword for job titles")
@click.option("--category", default="", help="Filter jobs by category")

def cli(search, category):
    jobs = fetch_jobs(search)

    if category:
        jobs = filter_by_category(jobs, category)

    if not jobs:
        print("No jobs found matching your criteria.")
        return

    for job in jobs[:10]:
        print(f"{job['company_name']} - {job['title']}")
