# Internship CLI

A Python-based command-line tool that fetches remote job listings, filters them by category or keyword, and detects new postings over time.

---

## Features

* Search remote jobs using keyword filters
* Filter jobs by category (e.g. Software Development)
* Detect and display **new job postings only**
* Persistent storage to avoid duplicate results
* Clean, formatted CLI output

---

## Tech Stack

* Python
* Click (CLI framework)
* Requests (API calls)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/saramihajlovic/internship-cli.git
cd internship-cli
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Search for jobs

```bash
python main.py search --search intern --category software --limit 5
```

---

### Check for new jobs

```bash
python main.py check-new --category software
```

---

## Project Structure

```
internship_cli/
│
├── main.py
├── cli.py
├── services/
├── storage/
├── utils/
├── data/
└── README.md
```

---

## Future Improvements

* Add notification system for new jobs
* Store timestamps for job tracking
* Support multiple job APIs
* Export results to CSV

---

## What I Learned

* Designing and structuring a CLI application
* Working with external APIs and JSON data
* Implementing persistent state and deduplication
* Improving user experience through CLI formatting

---

## Notes

This project uses the Remotive API to fetch remote job listings.
