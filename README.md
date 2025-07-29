# Aganitha AI Project Task – PubMed Paper Fetcher

This project provides a command-line tool to search PubMed for scientific research papers based on a given query (e.g., "cancer drug"), fetch paper details including authors and publication date, and filter authors affiliated with companies. The results are saved to a CSV file for easy analysis.

Features
Search PubMed using NCBI E-utilities API.

Fetch details like:

Paper title

Authors

Author affiliations

Publication date

Filter authors based on company affiliations.

Save search results into a CSV file.

Uses Poetry for easy dependency and environment management.

Tech Stack
Python 3.10+

Requests – For making HTTP requests to PubMed APIs

LXML – For parsing responses

Poetry – For package & virtual environment management

Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/<your-username>/aganitha-ai-project-task.git
cd aganitha-ai-project-task
Install Poetry (if not already installed)

bash
Copy
Edit
pip install poetry
Install dependencies

bash
Copy
Edit
poetry install
Usage
Run the CLI tool

bash
Copy
Edit
poetry run get-papers-list "cancer drug" -f result.csv -d
"cancer drug" → Search query

-f result.csv → Output CSV file

-d → Debug mode (optional)

Output

Results will be saved in result.csv.

Example Output
less
Copy
Edit
Searching for: cancer drug
Found 20 IDs: ['40721907', '40721888', ...]
Results saved to result.csv
Project Structure
graphql
Copy
Edit
aganitha_ai_project_task/
│
├── get_papers/
│   ├── cli.py        # CLI entry point
│   ├── fetch.py      # PubMed API fetching logic
│   ├── filter.py     # Author filtering logic
│   └── __init__.py
│
├── result.csv        # Output file (generated)
├── pyproject.toml    # Poetry configuration
└── README.md         # Project documentation
