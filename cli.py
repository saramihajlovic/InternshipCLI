import click

from services.job_service import fetch_jobs
from utils.filters import filter_by_category
from storage.repository import load_jobs, save_jobs

@click.group()
def cli():
    pass

@cli.command()
@click.option("--search", default="", help="Search keyword for job titles")
@click.option("--category", default="", help="Filter jobs by category")

def search(search, category):
    jobs = fetch_jobs(search)

    if category:
        jobs = filter_by_category(jobs, category)

    if not jobs:
        print("No jobs found matching your criteria.")
        return

    for job in jobs[:10]:
        print(f"{job['company_name']} - {job['title']}")

@cli.command(name="check-new")
@click.option("--search", default="", help="Search keyword for job titles")
@click.option("--category", default="", help="Filter jobs by category")

def check_new(search, category):
    old_jobs = load_jobs()
    new_jobs = fetch_jobs(search) or []

    if category:
        new_jobs = filter_by_category(new_jobs, category)

    # create a set of old urls that have been seen before
    old_urls = {job["url"] for job in old_jobs}

    # find new jobs not in old jobs list
    fresh_jobs = [job for job in new_jobs if job["url"] not in old_urls]

    if not fresh_jobs:
        print("No new jobs matching your criteria.")

    else:
        print(f"Located {len(fresh_jobs)} new jobs matching your criteria!\n")

        for job in fresh_jobs[:10]:
            print(f"{job['company_name']} - {job['title']}")
    save_jobs(old_jobs + fresh_jobs)
    