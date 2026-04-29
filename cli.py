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
@click.option("--limit", default=10, help="Limit the number of jobs displayed")

def search(search, category, limit):
    jobs = fetch_jobs(search)

    if category:
        jobs = filter_by_category(jobs, category)

    if not jobs:
        print("No jobs found matching your criteria.")
        return
    
    if limit <= 0:
        print("Please provide a positive number for the limit.")
        return

    for job in jobs[:limit]:
        print(f"{job['company_name']} - {job['title']}")

@cli.command(name="check-new")
@click.option("--search", default="", help="Search keyword for job titles")
@click.option("--category", default="", help="Filter jobs by category")
@click.option("--limit", default=10, help="Limit the number of new jobs displayed")
def check_new(search, category, limit):
    old_jobs = load_jobs()
    new_jobs = fetch_jobs(search) or []

    if category:
        new_jobs = filter_by_category(new_jobs, category)

    # create a set of old urls that have been seen before
    old_urls = {job["url"] for job in old_jobs}

    # find new jobs not in old jobs list
    fresh_jobs = [job for job in new_jobs if job["url"] not in old_urls]

    if limit <= 0:
        print("Please provide a positive number for the limit.")
        return

    if not fresh_jobs:
        print("No new jobs matching your criteria.")

    else:
        print(f"Located {len(fresh_jobs)} new jobs matching your criteria!\n")

        for job in fresh_jobs[:limit]:
            print(f"{job['company_name']} - {job['title']}")

    updated_jobs = old_jobs + fresh_jobs
    save_jobs(updated_jobs)
    