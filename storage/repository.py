import json
import os

FILE_PATH = "data/jobs.json"

def load_jobs():
    """Load jobs from the JSON file. If the file doesn't exist or is empty, return an empty list."""
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
        content = f.read().strip()

        if not content:
            return []
        
        return json.loads(content)
    except json.JSONDecodeError:
        return []

def save_jobs(jobs):
    """Save the list of jobs to the JSON file, overwriting any existing content."""
    with open(FILE_PATH, "w") as f:
        json.dump(jobs, f, indent=2)