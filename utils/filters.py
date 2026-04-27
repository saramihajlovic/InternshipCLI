def filter_by_category(jobs, category):

    filtered_jobs = [job for job in jobs if category in job["category"].lower()]
    return filtered_jobs