def filter_by_category(jobs, category):
    """Filter a list of jobs by a specified category, returning only those that match the category criteria."""
    filtered_jobs = [job for job in jobs if category in job["category"].lower()]
    return filtered_jobs